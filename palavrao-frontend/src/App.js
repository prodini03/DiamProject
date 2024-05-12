import React, {useState, useEffect} from 'react';
import './App.css';
import Header from './Header';
import Comments from './Comments'

function App() {
    return (
        <>
            <Header/>
            <Comments/>
        </>
    );
}

export default App;