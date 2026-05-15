
[     UTC     ] Logs for market-analysis-app-gncnvfvulqeravbzp884ie.streamlit.app/
────────────────────────────────────────────────────────────────────────────────────────
[07:53:50] 🖥 Provisioning machine...
[07:53:56] 🎛 Preparing system...
[07:53:54] 🚀 Starting up repository: 'market-analysis-app', branch: 'main', main module: 'app.py'
[07:53:54] 🐙 Cloning repository...
[07:53:54] 🐙 Cloning into '/mount/src/market-analysis-app'...

[07:53:54] 🐙 Cloned repository!
[07:53:54] 🐙 Pulling code changes from Github...
[07:53:54] 📦 Processing dependencies...

──────────────────────────────────────── uv ───────────────────────────────────────────

Using uv pip install.
Using Python 3.14.4 environment at /home/adminuser/venv
Resolved 57 packages in 460ms
Prepared 57 packages in 1.48s
Installed 57 packages in 65ms
 + altair==6.1.0
 + anyio==4.13.0
 + attrs==26.1.0
 + beautifulsoup4==4.14.3
 + blinker==1.9.0
 + cachetools==7.1.1
 + certifi==2026.4.22
 + cffi==2.0.0
 + charset-normalizer==3.4.7[2026-05-15 07:53:57.163265] 
 + click==8.3.3
 + curl-cffi==0.15.0
 + frozendict==2.4.7
 + gitdb==4.0.12
 + gitpython==3.1.50
 + h11==0.16.0
 + httptools==0.7.1
 [2026-05-15 07:53:57.163502] + idna==3.15
 + itsdangerous==2.2.0
 + jinja2==3.1.6
 + jsonschema==4.26.0
 + jsonschema-specifications==2025.9.1
 + markdown-it-py==4.2.0
 + markupsafe==3.0.3
 + mdurl==0.1.2
 + multitasking[2026-05-15 07:53:57.163632] ==0.0.13
 + narwhals==2.21.0
 + numpy==2.4.4
 + packaging==26.2
 + pandas==3.0.3
 [2026-05-15 07:53:57.163752] + peewee==4.0.5
 + pillow==12.2.0
 + platformdirs==4.9.6
 + protobuf==7.34.1
 + pyarrow==24.0.0
 + pycparser[2026-05-15 07:53:57.163912] ==3.0
 + pydeck==0.9.2
 + pygments==2.20.0
 + python-dateutil==2.9.0.post0
 + python-multipart==0.0.28
 + pytz==2026.2
 + referencing==0.37.0
 + requests==2.34.2[2026-05-15 07:53:57.164058] 
 + rich==15.0.0
 + rpds-py==0.30.0
 + six==1.17.0
 + smmap==5.0.3
 + soupsieve==2.8.3
 + starlette[2026-05-15 07:53:57.164195] ==1.0.0
 + streamlit==1.57.0
 + tenacity==9.1.4
 + toml==0.10.2
 + typing-extensions==4.15.0
 + urllib3==2.7.0
 + uvicorn==0.47.0
 + [2026-05-15 07:53:57.164280] watchdog==6.0.0
 + websockets==16.0
 + yfinance==1.3.0
Checking if Streamlit is installed
Found Streamlit version 1.57.0 in the environment
Installing rich for an improved exception logging
Using uv pip install.
Using Python 3.14.4 environment at /home/adminuser/venv
Audited 1 package in 2ms

────────────────────────────────────────────────────────────────────────────────────────

[07:53:58] 🐍 Python dependencies were installed from /mount/src/market-analysis-app/requirements.txt using uv.
Check if streamlit is installed
Streamlit is already installed
[07:53:59] 📦 Processed dependencies!
2026-05-15 07:54:00.893 Uvicorn server started on 0.0.0.0:8501



[07:54:01] ⛓ Spinning up manager process...
────────────────────── Traceback (most recent call last) ───────────────────────
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:129 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:689 in code_to_exec                                     
                                                                                
  /mount/src/market-analysis-app/app.py:3 in <module>                           
                                                                                
      1 import streamlit as st                                                  
      2 import yfinance as yf                                                   
  ❱   3 import pandas_ta as ta                                                  
      4 import pandas as pd                                                     
      5                                                                         
      6 st.set_page_config(page_title="Share Market Option Signals", layout="w  
────────────────────────────────────────────────────────────────────────────────
ModuleNotFoundError: No module named 'pandas_ta'
────────────────────── Traceback (most recent call last) ───────────────────────
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:129 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:689 in code_to_exec                                     
                                                                                
  /mount/src/market-analysis-app/app.py:3 in <module>                           
                                                                                
      1 import streamlit as st                                                  
      2 import yfinance as yf                                                   
  ❱   3 import pandas_ta as ta                                                  
      4 import pandas as pd                                                     
      5                                                                         
      6 st.set_page_config(page_title="Share Market Option Signals", layout="w  
────────────────────────────────────────────────────────────────────────────────
ModuleNotFoundError: No module named 'pandas_ta'
────────────────────── Traceback (most recent call last) ───────────────────────
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:129 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:689 in code_to_exec                                     
                                                                                
  /mount/src/market-analysis-app/app.py:3 in <module>                           
                                                                                
      1 import streamlit as st                                                  
      2 import yfinance as yf                                                   
  ❱   3 import pandas_ta as ta                                                  
      4 import pandas as pd                                                     
      5                                                                         
      6 st.set_page_config(page_title="Share Market Option Signals", layout="w  
────────────────────────────────────────────────────────────────────────────────
ModuleNotFoundError: No module named 'pandas_ta'
