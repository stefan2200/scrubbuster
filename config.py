configuration = {
    "ProFTPD" : {
        "port" : 21,
        "banner" : "220 ProFTPD 1.3.1 Server (ProFTPD)\n",
        "calls" : {
            "cprf" : "350 OK",
            "default" : "350"
            },
        "errors" : {
            "CPFR" : True,
            "auth" : True
        }
    },
     "Telnet" : {
        "port" : 23,
        "banner" : "Login:",
        "calls" : {
            "administrator" : "password:",
            "default" : ""
            },
        "errors" : {
            "administrator" : True
        }
    },
    "BIND" : {
        "port" : 53,
        "banner" : "BIND 4.0.32 Ready\n",
        "calls" : {
            "help" : "Not Implemented\n",
            "default" : "350"
            },
        "errors" : {
            "lookup" : True,
            "resolve" : True
        }
    }
} 
