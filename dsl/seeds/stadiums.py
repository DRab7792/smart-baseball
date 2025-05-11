import pandas as pd
from pybaseball import park_codes
from datasources.lahman import parks
from sqlalchemy import text

def truncate_stadiums(db):
    db.execute(text("TRUNCATE TABLE stadiums RESTART IDENTITY CASCADE"))
    db.execute(text("ALTER SEQUENCE stadiums_id_seq RESTART WITH 1"))


def seed_stadiums(db, truncate=False):
    if truncate:
        truncate_stadiums(db)

    rs_parks = park_codes()
    lh_parks = parks()
    ac_parks = pd.read_csv('./datasources/andrew_clem_stadiums.csv')
    ac_parks = transform_ac_parks(ac_parks)

    rs_parks = rs_parks.drop(columns=['city', 'state'])

    # Join rs_parks with lh_parks on park_id/parkkey
    parks_df = pd.merge(
        rs_parks,
        lh_parks,
        left_on='park_id',
        right_on='parkkey',
        how='left'
    )
    
    # Join parks_df with ac_parks on name
    parks_df = pd.merge(
        parks_df,
        ac_parks,
        left_on='name',
        right_on='name',
        how='left'
    )
    

    parks_df = parks_df.drop(columns=['ID', 'park_id', 'parkname'])
    parks_df = parks_df.rename(columns={
        'parkkey': 'rs_id',
    })

    # Remove rows where rs_id is null/NaN
    # parks_df = parks_df.dropna(subset=['rs_id'])

    # Convert open and close columns to dates
    parks_df['open'] = pd.to_datetime(parks_df['open'], errors='coerce')
    parks_df['close'] = pd.to_datetime(parks_df['close'], errors='coerce')

    print (parks_df.head())
    print (parks_df.columns)

    # Insert into stadiums table
    for index, row in parks_df.iterrows():
        db.execute(
            text("""
            INSERT INTO stadiums (
                name,
                nickname,
                open,
                close,
                league,
                notes,
                parkalias,
                rs_id,
                city,
                state,
                country,
                mlb_lifetime,
                seating_capacity,
                first_deck_seating_rows,
                mez_second_deck_seating_rows,
                upper_deck_seating_rows,
                lower_deck_overhang_pct,
                upper_deck_overhang_pct,
                fair_territory_sqft,
                foul_territory_sqft,
                lf_fence_height,
                cf_fence_height,
                rf_fence_height,
                cf_orientation,
                backstop,
                left_field_distance,
                left_center_distance,
                center_field_distance,
                right_center_distance,
                right_field_distance
            ) VALUES (
                :name,
                :nickname,
                :open,
                :close,
                :league,
                :notes,
                :parkalias,
                :rs_id,
                :city,
                :state,
                :country,
                :mlb_lifetime,
                :seating_capacity,
                :first_deck_seating_rows,
                :mez_second_deck_seating_rows,
                :upper_deck_seating_rows,
                :lower_deck_overhang_pct,
                :upper_deck_overhang_pct,
                :fair_territory_sqft,
                :foul_territory_sqft,
                :lf_fence_height,
                :cf_fence_height,
                :rf_fence_height,
                :cf_orientation,
                :backstop,
                :left_field_distance,
                :left_center_distance,
                :center_field_distance,
                :right_center_distance,
                :right_field_distance
            )
            ON CONFLICT (rs_id) DO NOTHING
            """),
            {
                'name': clean_nan(row['name']),
                'nickname': clean_nan(row['nickname']), 
                'open': clean_nan(row['open']),
                'close': clean_nan(row['close']),
                'league': clean_nan(row['league']),
                'notes': clean_nan(row['notes']),
                'parkalias': clean_nan(row['parkalias']),
                'rs_id': clean_nan(row['rs_id']),
                'city': clean_nan(row['city']),
                'state': clean_nan(row['state']),
                'country': clean_nan(row['country']),
                'mlb_lifetime': clean_nan(row['mlb_lifetime']),
                'seating_capacity': clean_nan(row['seating_capacity']),
                'first_deck_seating_rows': clean_nan(row['first_deck_seating_rows']),
                'mez_second_deck_seating_rows': clean_nan(row['mez_second_deck_seating_rows']),
                'upper_deck_seating_rows': clean_nan(row['upper_deck_seating_rows']),
                'lower_deck_overhang_pct': clean_nan(row['lower_deck_overhang_pct']),
                'upper_deck_overhang_pct': clean_nan(row['upper_deck_overhang_pct']),
                'fair_territory_sqft': clean_nan(row['fair_territory_sqft']),
                'foul_territory_sqft': clean_nan(row['foul_territory_sqft']),
                'lf_fence_height': clean_nan(row['lf_fence_height']),
                'cf_fence_height': clean_nan(row['cf_fence_height']), 
                'rf_fence_height': clean_nan(row['rf_fence_height']),
                'cf_orientation': clean_nan(row['cf_orientation']),
                'backstop': clean_nan(row['backstop']),
                'left_field_distance': clean_nan(row['left_field_distance']),
                'left_center_distance': clean_nan(row['left_center_distance']),
                'center_field_distance': clean_nan(row['center_field_distance']),
                'right_center_distance': clean_nan(row['right_center_distance']),
                'right_field_distance': clean_nan(row['right_field_distance']),
                
            }
        )
        db.commit()

    

    return parks_df

def transform_ac_parks(ac_parks):
    ac_parks = ac_parks.rename(columns={
        'Stadium (see notes)': 'name',
        'MLB lifetime (years thru 2024)': 'mlb_lifetime',
        'Seating capacity (at peak)': 'seating_capacity',
        '1st deck Seating Rows': 'first_deck_seating_rows',
        'Mez. / 2nd deck Seating Rows': 'mez_second_deck_seating_rows',
        'Upper deck Seating Rows': 'upper_deck_seating_rows',
        'Lower deck Overhang': 'lower_deck_overhang_pct',
        'Upper deck Overhang': 'upper_deck_overhang_pct',
        'Fair Territory (1,000 sq. ft.)': 'fair_territory_sqft',
        'Foul Territory (1,000 sq. ft.)': 'foul_territory_sqft',
        'LF Fence Height': 'lf_fence_height',
        'CF Fence Height': 'cf_fence_height',
        'RF Fence Height': 'rf_fence_height',
        'CF Orientation': 'cf_orientation',
        'Backstop': 'backstop',
        'Left field distance': 'left_field_distance',
        'Left-center distance': 'left_center_distance',
        'Center field distance': 'center_field_distance',
        'Right-center distance': 'right_center_distance',
        'Right field distance': 'right_field_distance'
    })
    ac_parks = ac_parks.drop(columns=['Team(s)'])

    
    # Remove commas, '+', and any other non-numeric characters, then convert to int
    ac_parks['seating_capacity'] = ac_parks['seating_capacity'].str.replace(',', '').str.replace(r'[^\d.]', '', regex=True).astype(int)
    ac_parks['first_deck_seating_rows'] = pd.to_numeric(ac_parks['first_deck_seating_rows'].str.replace(r'[^\d.]', '', regex=True), errors='coerce')
    ac_parks['mez_second_deck_seating_rows'] = pd.to_numeric(ac_parks['mez_second_deck_seating_rows'].str.replace(r'[^\d.]', '', regex=True), errors='coerce')
    ac_parks['upper_deck_seating_rows'] = pd.to_numeric(ac_parks['upper_deck_seating_rows'].str.replace(r'[^\d.]', '', regex=True), errors='coerce')

    ac_parks['fair_territory_sqft'] = ac_parks['fair_territory_sqft'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float) * 1000
    ac_parks['foul_territory_sqft'] = ac_parks['foul_territory_sqft'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float) * 1000

    ac_parks['backstop'] = pd.to_numeric(ac_parks['backstop'].str.replace(r'[^\d.]', '', regex=True), errors='coerce')
    ac_parks['mlb_lifetime'] = pd.to_numeric(ac_parks['mlb_lifetime'].astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce')

    ac_parks['lower_deck_overhang_pct'] = pd.to_numeric(ac_parks['lower_deck_overhang_pct'].astype(str).str.replace('%', '').str.replace(r'[^\d.]', '', regex=True), errors='coerce')
    ac_parks['upper_deck_overhang_pct'] = pd.to_numeric(ac_parks['upper_deck_overhang_pct'].astype(str).str.replace('%', '').str.replace(r'[^\d.]', '', regex=True), errors='coerce')

    ac_parks['lf_fence_height'] = pd.to_numeric(ac_parks['lf_fence_height'].astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce')
    ac_parks['cf_fence_height'] = pd.to_numeric(ac_parks['cf_fence_height'].astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce')
    ac_parks['rf_fence_height'] = pd.to_numeric(ac_parks['rf_fence_height'].astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce')

    ac_parks['left_field_distance'] = ac_parks['left_field_distance'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(int)
    ac_parks['left_center_distance'] = ac_parks['left_center_distance'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(int)
    ac_parks['center_field_distance'] = ac_parks['center_field_distance'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(int)
    ac_parks['right_center_distance'] = ac_parks['right_center_distance'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(int)
    ac_parks['right_field_distance'] = ac_parks['right_field_distance'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(int)

    return ac_parks
def clean_nan(value):
    return None if pd.isna(value) else value
