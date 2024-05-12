import React from 'react';
import logo from './logo.png';

console.log(logo);

function Header() {
    return (
        <>
            <head>
                <link rel="preconnect" href="https://fonts.googleapis.com"/>
                <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin/>
                <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;400;700&display=swap"
                      rel="stylesheet"/>
                <link rel="stylesheet" type="text/css"
                      href="https://cdn.jsdelivr.net/npm/toastify-js/src/toastify.min.css"/>
                <link rel="stylesheet" type="text/css" href="{% static 'palavrao/style.css' %}"/>
                <link rel="stylesheet" type="text/css" href="{% static 'palavrao/stylecomment.css' %}"/>
                <meta charSet="UTF-8"/>
                <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Karma"/>
            </head>
            <h1 style={{textAlign: 'center'}}>
                <img src={logo} width="400" height="100" alt="Palavrão"/>
            </h1>
        </>
    );
}

export default Header;