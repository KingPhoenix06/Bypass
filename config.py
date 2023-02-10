import os
import logging
class Config:
    API_ID = int(os.environ.get("API_ID", "3369707"))
    API_HASH = os.environ.get("API_HASH", "aec1fd7abdfec322c426961a570ef336")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5929947495:AAGlrMiE1Lj48hGW-ey_m_jPXI5Huknyeuw")
    Channel_id = os.environ.get("Channel_id", "-1001265144942")
    Drivebuzz_crypt = os.environ.get("Drivebuzz_crypt", "")
    Drivefire_crypt = os.environ.get("Drivefire_crypt", "")
    Jiodrive_crypt = os.environ.get("Jiodrive_crypt", "")
    Gadrive_crypt = os.environ.get("Gadrive_crypt", "")
    Kolop_crypt = os.environ.get("Kolop_crypt", "")
    Katdrive_crypt = os.environ.get("Katdrive_crypt", "")
    Gtot_crypt = os.environ.get("Gtot_crypt", "")
    Appdrive_email = os.environ.get("Appdrive_email", "")
    Appdrive_password = os.environ.get("Appdrive_password", "")
    Hubdrive_crypt = os.environ.get("Hubdrive_crypt", "")
    Sharerpw_xsrf_token = os.environ.get("Sharerpw_xsrf_token", "")
    Sharerpw_laravel_session = os.environ.get("Sharerpw_laravel_session", "")
