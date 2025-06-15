{{ config(
    materialized='table',
    unique_key='id'
) }}


WITH source AS(
    select * 
    from {{ source('dev','raw_weather_data') }}
),


 del_dup as (
    SELECT *,row_number() over(partition by time order by inserted_at) as row_number
    from source
)




SELECT  id,city,temperature,weather_descriptions,wind_speed,time as weather_time_local,(inserted_at + (utc_offset || 'hours')::interval) as inserted_at_local FROM del_dup where row_number = 1