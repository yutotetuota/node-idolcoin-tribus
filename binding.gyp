{
    "targets": [
        {
            "target_name": "idolcoin_tribus",
            "sources": [               
                "idolcoin_tribus.cc",
                "tribus/tribus.c",
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}
