import React from 'react';

function Header() {
    function w3_open() {
        document.getElementById("mySidebar").style.display = "block";
    }

    function w3_close() {
        document.getElementById("mySidebar").style.display = "none";
    }
    return (
        <>
            <head>
                <meta charSet="UTF-8"/>
                <meta httpEquiv="X-UA-Compatible" content="IE=edge"/>
                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                <title>Title</title>
                <link rel="preconnect" href="https://fonts.googleapis.com"/>
                <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true"/>
                <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;400;700&display=swap"
                      rel="stylesheet"/>
                <link rel="stylesheet" type="text/css"
                      href="https://cdn.jsdelivr.net/npm/toastify-js/src/toastify.min.css"/>
                <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"/>
                <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Karma"/>
            </head>
            <div className="text-center">
                <img
                    src="/iscte.avif" // (1)
                    width="600"
                    alt="ISCTE"
                    className="img-thumbnail"
                    style={{marginTop: "20px"}} // (2)
                />
            </>
            );
            }
            export default Header;