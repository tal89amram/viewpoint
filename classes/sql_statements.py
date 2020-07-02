# Holds all SQL statements for the program
# The only class that should ever interact with is the SQL_Controller


class SQLStatements:

    # Select by ID and index
    def select_by_ids_picture(self, hike_id: int, index_in_hike: int) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} AND \
            index_in_hike={index}'.format(id=hike_id, index=index_in_hike)
        return statement

    # Projector
    # --------------------------------------------------------------------------

    # ******************************     Time     ******************************

    # Time - first & last across hikes
    def select_by_time_first_picture(self) -> str:
        statement = 'SELECT * FROM pictures ORDER BY time ASC LIMIT 1'
        return statement

    def select_by_time_last_picture(self) -> str:
        statement = 'SELECT * FROM pictures ORDER BY time DESC LIMIT 1'
        return statement

    # Time - next & previous across hikes
    def select_by_time_next_picture(self, time: float) -> str:
        statement = 'SELECT * FROM pictures WHERE time>{t} \
            ORDER BY time ASC LIMIT 1'.format(t=time)
        return statement

    def select_by_time_previous_picture(self, time: float) -> str:
        statement = 'SELECT * FROM pictures WHERE time<{t} \
            ORDER BY time DESC LIMIT 1'.format(t=time)
        return statement

    # Time - first & last in a hike
    def select_by_time_first_picture_in_hike(self, hike_id: float) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} \
            ORDER BY time ASC LIMIT 1'.format(id=hike_id)
        return statement

    def select_by_time_last_picture_in_hike(self, hike_id: float) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} \
            ORDER BY time DESC LIMIT 1'.format(id=hike_id)
        return statement

    # Time - next & previous in a hike
    def select_by_time_next_picture_in_hike(self, hike_id: float, time: float) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} AND time>{t} \
            ORDER BY time ASC LIMIT 1'.format(id=hike_id, t=time)
        return statement

    def select_by_time_previous_picture_in_hike(self, hike_id: float, time: float) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} AND time<{t} \
            ORDER BY time DESC LIMIT 1'.format(id=hike_id, t=time)
        return statement

    # ****************************     Altitude     ****************************

    # Altitude - greatest & least across hikes
    def select_by_altitude_greatest_picture(self) -> str:
        statement = 'SELECT * FROM pictures ORDER BY altitude DESC LIMIT 1'
        return statement

    def select_by_altitude_least_picture(self) -> str:
        statement = 'SELECT * FROM pictures ORDER BY altitude ASC LIMIT 1'
        return statement

    # Altitude - count of same altitude across hikes
    def find_size_by_altitude_greater_time(self, altitude: float, time: float) -> str:
        statement = 'SELECT count(*) FROM pictures WHERE altitude={alt} \
            AND time>{t}'.format(alt=altitude, t=time)
        return statement

    def find_size_by_altitude_less_time(self, altitude: float, time: float) -> str:
        statement = 'SELECT count(*) FROM pictures WHERE altitude={alt} \
            AND time<{t}'.format(alt=altitude, t=time)
        return statement

    # Altitude - next across hikes
    def select_by_greater_altitude_next_picture(self, altitude: float) -> str:
        statement = 'SELECT * FROM pictures WHERE altitude>{alt} \
            ORDER BY altitude ASC, time ASC LIMIT 1'.format(alt=altitude)
        return statement

    def select_by_equal_altitude_next_picture(self, altitude: float, time: float) -> str:
        statement = 'SELECT * FROM pictures WHERE altitude={alt} AND \
            time>{t} ORDER BY altitude ASC, time ASC LIMIT 1'.format(alt=altitude, t=time)
        return statement

    # Altitude - previous across hikes
    def select_by_less_altitude_previous_picture(self, altitude: float) -> str:
        statement = 'SELECT * FROM pictures WHERE altitude<{alt} \
            ORDER BY altitude DESC, time DESC LIMIT 1'.format(alt=altitude)
        return statement

    def select_by_equal_altitude_previous_picture(self, altitude: float, time: float) -> str:
        statement = 'SELECT * FROM pictures WHERE altitude={alt} AND \
            time<{t} ORDER BY altitude DESC, time DESC LIMIT 1'.format(alt=altitude, t=time)
        return statement

    # Altitude - greatest and least in a hike
    def select_by_altitude_greatest_picture_in_hike(self, hike_id: float) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} \
            ORDER BY altitude DESC LIMIT 1'.format(id=hike_id)
        return statement

    def select_by_altitude_least_picture_in_hike(self, hike_id: float) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} \
            ORDER BY altitude ASC LIMIT 1'.format(id=hike_id)
        return statement

    # Altitude - count of same altitude in a hike
    def find_size_by_altitude_greater_time_in_hike(self, hike_id: float,
                                                   altitude: float, time: float) -> str:
        statement = 'SELECT count(*) FROM pictures WHERE hike={id} AND altitude={alt} \
            AND time>{t}'.format(id=hike_id, alt=altitude, t=time)
        return statement

    def find_size_by_altitude_less_time_in_hike(self, hike_id: float,
                                                altitude: float, time: float) -> str:
        statement = 'SELECT count(*) FROM pictures WHERE hike={id} AND altitude={alt} \
            AND time<{t}'.format(id=hike_id, alt=altitude, t=time)
        return statement

    # Altitdue - next in a hike
    def select_by_greater_altitude_next_picture_in_hike(self, hike_id: float,
                                                        altitude: float) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} AND altitude>{alt} \
            ORDER BY altitude ASC, time ASC LIMIT 1'.format(id=hike_id, alt=altitude)
        return statement

    def select_by_equal_altitude_next_picture_in_hike(self, hike_id: float,
                                                      altitude: float, time: float) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} AND altitude={alt} AND \
            time>{t} ORDER BY altitude ASC, time ASC LIMIT 1'.format(id=hike_id, alt=altitude, t=time)
        return statement

    # Altitdue - previous in a hike
    def select_by_less_altitude_previous_picture_in_hike(self, hike_id: float,
                                                         altitude: float) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} AND altitude<{alt} \
            ORDER BY altitude DESC, time DESC LIMIT 1'.format(id=hike_id, alt=altitude)
        return statement

    def select_by_equal_altitude_previous_picture_in_hike(self, hike_id: float,
                                                          altitude: float, time: float) -> str:
        statement = 'SELECT * FROM pictures WHERE hike={id} AND altitude={alt} AND \
            time<{t} ORDER BY altitude DESC, time DESC LIMIT 1'.format(id=hike_id, alt=altitude, t=time)
        return statement

    # Color
    # def select_by_color_next_picture() -> str:

    # def select_by_color_previous_picture() -> str:

    # Hike
    def select_size_of_hike(self, hike_id: float) -> str:
        statement = 'SELECT pictures FROM hikes WHERE hike_id={id}'.format(id=hike_id)
        return statement

    def select_hike_by_id(self, hike_id: float) -> str:
        statement = 'SELECT * FROM hikes WHERE hike_id={id}'.format(id=hike_id)
        return statement

    # Camera
    # --------------------------------------------------------------------------
    def select_hike_count(self) -> str:
        statement = 'SELECT count(*) FROM hikes'
        return statement

    def select_last_hike_id(self) -> str:
        statement = 'SELECT hike_id FROM hikes ORDER BY hike_id DESC LIMIT 1'
        return statement

    def select_last_hike_end_time(self) -> str:
        statement = 'SELECT end_time FROM hikes ORDER BY end_time DESC LIMIT 1'
        return statement

    def select_last_photo_index_of_hike(self, hike_id: int) -> str:
        statement = 'SELECT index_in_hike FROM pictures WHERE hike={n} \
            ORDER BY index_in_hike DESC LIMIT 1'.format(n=hike_id)
        return statement

    def select_last_altitude_recorded(self) -> str:
        statement = 'SELECT altitude FROM pictures ORDER BY ROWID DESC LIMIT 1'
        return statement

    def select_last_row_id(self) -> str:
        statement = 'SELECT ROWID FROM pictures ORDER BY ROWID DESC LIMIT 1'
        return statement

    def insert_new_hike(self, time: float) -> str:
        statement = 'INSERT INTO hikes(start_time, end_time, pictures) VALUES({t}, {t}, 0)'.format(t=time)
        return statement

    def insert_new_picture(self, time: float, hike_id: int, photo_index: int) -> str:
        statement = 'INSERT INTO pictures(time, hike, index_in_hike) VALUES \
            ({t}, {h}, {p})'.format(t=time, h=hike_id, p=photo_index)
        return statement

    def update_picture_image_path(self, cam_num: int, path: str, hike_id: int, photo_index: int) -> str:
        # Only difference between statements is cameraX=
        if cam_num == 1:
            statement = 'UPDATE pictures SET camera1="{p}", updated_date_time=datetime() \
                WHERE hike={h} AND index_in_hike={i} \
                    '.format(p=path, h=hike_id, i=photo_index)
        elif cam_num == 2:
            statement = 'UPDATE pictures SET camera2="{p}", updated_date_time=datetime() \
                WHERE hike={h} AND index_in_hike={i} \
                    '.format(p=path, h=hike_id, i=photo_index)
        elif cam_num == 3:
            statement = 'UPDATE pictures SET camera3="{p}", updated_date_time=datetime() \
                WHERE hike={h} AND index_in_hike={i} \
                    '.format(p=path, h=hike_id, i=photo_index)
        else:
            raise Exception('cam_num should be 1, 2, or 3. The value was: {n}'.format(n=cam_num))

        return statement

    def update_picture_altitude(self, altitude: float, hike_id: int, photo_index: int) -> str:
        statement = 'UPDATE pictures SET altitude={a}, updated_date_time=datetime() \
            WHERE hike={h} AND index_in_hike={p}'.format(a=altitude, h=hike_id, p=photo_index)
        print(statement)
        return statement

    def update_picture_altitude_for_id(self, altitude: float, rowid: int) -> str:
        statement = 'UPDATE  pictures SET altitude={a}, updated_date_time=datetime() \
            WHERE ROWID={r}'.format(a=altitude, r=rowid)
        return statement

    def update_hike_path(self, path: str, hike_id: int) -> str:
        statement = 'UPDATE hikes SET path="{p}", updated_date_time=datetime() \
            WHERE hike_id={h}'.format(p=path, h=hike_id)
        return statement

    def update_hike_endtime_picture_count(self, time: float, count: int, hike_id: int) -> str:
        statement = 'UPDATE hikes SET end_time={t}, pictures={c}, updated_date_time=datetime() WHERE hike_id={h} \
            '.format(t=time, c=count, h=hike_id)
        return statement

    # Transfer
    # --------------------------------------------------------------------------
    def select_valid_photos_in_given_hike(self, hike_id: int) -> int:
        # TODO: update the MAX value to Mt. Everest
        statement = 'SELECT * FROM pictures WHERE hike == {h} AND altitude < 10000 AND altitude >= 0 AND \
            camera1 IS NOT NULL AND camera2 IS NOT NULL AND camera3 IS NOT NULL'.format(h=hike_id)
        return statement

    def upsert_picture_row(self, time: float, hike: int, index_in_hike: int, altitude: float, hue: float, saturation: float, value: float, red: float, green: float, blue: float, camera1: str, camera2: str, camera3: str, camera_landscape: str) -> int:
        statement = 'INSERT OR REPLACE INTO pictures \
            (time, hike, index_in_hike, altitude, hue, saturation, value, red, green, blue, camera1, camera2, camera3, camera_landscape) \
            VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, "{}", "{}", "{}", "{}")\
            '.format(time, hike, index_in_hike, altitude, hue, saturation, value, red, green, blue, camera1, camera2, camera3, camera_landscape)
        return statement

    def upsert_hike_row(self, hike_id: int, avg_altitude: float, avg_hue: float, avg_saturation: float, avg_value: float, start_time: float, end_time: float, pictures: int, path: str) -> str:
        statement = 'INSERT OR REPLACE INTO hikes \
            (hike_id, avg_altitude, avg_hue, avg_saturation, avg_value, start_time, end_time, pictures, path) \
            VALUES ({}, {}, {}, {}, {}, {}, {}, {}, "{}")\
            '.format(hike_id, avg_altitude, avg_hue, avg_saturation, avg_value, start_time, end_time, pictures, path)
        return statement

    def get_hike_average_color(self, hike_id: int):
        statement = 'SELECT avg_hue, avg_saturation, avg_value FROM hikes WHERE hike_id == {}'.format(hike_id)
        return statement

    def get_size_of_hike(self, hike_id: int):
        statement = 'SELECT pictures FROM hikes WHERE hike_id == {}'.format(hike_id)
        return statement

    def get_picture_with_timestamp(self, time: float):
        statement = 'SELECT count(*) FROM pictures WHERE time == {}'.format(time)
        return statement

    def get_dominant_color_for_picture_of_given_timestamp(self, time: float):
        statement = 'SELECT hue, saturation, value FROM pictures WHERE time == {}'.format(time)
        return statement

    def delete_pictures(self) -> str:
        statement = 'DELETE FROM pictures'
        return statement

    def delete_hikes(self) -> str:
        statement = 'DELETE FROM hikes'
        return statement

    def get_hike_path(self, hike_id: int) -> str:
        statement = "SELECT path FROM hikes WHERE hike_id == {}".format(hike_id)
        return statement
