SAP B1 Assistant — Mini (Laptop + Remote Server)
======================================================

इसे आप अपने लैपटॉप पर चला सकते हैं, भले ही आपका SAP B1 सर्वर कहीं और हो।
बस लैपटॉप से सर्वर तक नेटवर्क पहुंच (VPN/Static IP) होनी चाहिए।

A. क्या-क्या चाहिए
------------------
1) Python 3.10+ (Windows पर इंस्टॉल करें)
2) Microsoft ODBC Driver for SQL Server (v17 या v18) — नाम आमतौर पर:
   - "ODBC Driver 17 for SQL Server" या
   - "ODBC Driver 18 for SQL Server"
3) SQL Server तक पहुंच (VPN/Static IP) और एक READ-ONLY DB user (Server, DB, Username, Password)

B. कैसे चलाएं (Step-by-step)
----------------------------
1) Command Prompt खोलें और इस फ़ोल्डर में जाएँ.
2) Packages install करें:
   pip install -r requirements.txt

3) App चलाएँ:
   streamlit run sap_assistant_min.py

4) ब्राउज़र में जो पेज खुलेगा उस पर ये भरें:
   - SQL Server (hostname/IP)
   - Database (e.g., SBODemoUS)
   - Username (read-only)
   - Password
   - Driver name: ODBC Driver 17 for SQL Server

5) "Test Connection" दबाएँ।
   - Success दिखे तो आगे बढ़ें
   - Error हो तो:
     • VPN connected है? 
     • SQL Server port 1433 खुला है?
     • Username/Password सही है?
     • Driver नाम सही लिखा है?

6) नीचे "Sales by Customer (Month)" में Year/Month भरें, SlpCode optional, "Run Report" दबाएँ.

C. Notes
--------
- यह केवल READ-ONLY रिपोर्टिंग करता है (SAFE).
- अगर आपका SAP HANA है, तो यह मिनी ऐप सीधे HANA के लिए नहीं है (SQL Server के लिए है)। HANA के लिए अलग ड्राइवर/कोड लगेगा.
- Service Layer (B1) इस मिनी में शामिल नहीं है — बाद में जोड़ सकते हैं।
