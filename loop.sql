DO $$
  DECLARE
    prov_id Provinces.province_id%TYPE;
    prov_name Provinces.province_name%TYPE;
    
  BEGIN
    prov_id := 7;
    prov_name := 'Province';
    FOR counter IN 1..5
      LOOP
        INSERT INTO Provinces (province_id, province_name)
        VALUES (counter || prov_id, prov_name || counter + 7);
      END LOOP;
  END;
$$

SELECT * FROM provinces