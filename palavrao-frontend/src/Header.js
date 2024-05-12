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
                <link rel="stylesheet" type="text/css" href="{% static 'palavrao/style.css' %}"/>
                <link rel="stylesheet" type="text/css" href="{% static 'palavrao/stylecomment.css' %}"/>
                <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"/>
                <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Karma"/>
                <style>
                    {`
                    h1, h2, h3, h4, h5, h6 {
                        font-family: "Karma", sans-serif;
                    }

                    .w3-bar-block .w3-bar-item {
                        padding: 20px;
                    }
                `}
                </style>
            </head>
            <nav className="w3-sidebar w3-bar-block w3-card w3-top w3-xlarge w3-animate-left"
                 style={{display: 'none', zIndex: 2, width: '40%', minWidth: '300px'}} id="mySidebar">
                <a href="javascript:void(0)" onClick={w3_close} className="w3-bar-item w3-button">Close Menu</a>
                    <>
                        <a href="{% url 'palavrao:dados_pessoais' %}" className="w3-bar-item w3-button">Dados
                            Pessoais</a>
                        <a href="{% url 'palavrao:comentarios' %}" className="w3-bar-item w3-button">Comentarios</a>
                        <a href="{% url 'palavrao:logoutview' %}" className="w3-bar-item w3-button">Logout</a>
                    </>
                    <>
                        <a href="{% url 'palavrao:criarconta' %}" className="w3-bar-item w3-button">Criar conta</a>
                        <a href="{% url 'palavrao:login' %}" className="w3-bar-item w3-button">Login</a>
                    </>
            </nav>
            <div className="w3-top">
                <div className="w3-white w3-xlarge" style={{maxWidth: '1200px', margin: 'auto'}}>
                    <div className="w3-button w3-padding-16 w3-left" onClick={w3_open}
                         style={{backgroundColor: '#fdfaf2'}}>☰
                    </div>
                </div>
            </div>
        </>
    );
}

export default Header;