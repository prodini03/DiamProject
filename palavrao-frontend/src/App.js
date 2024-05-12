import React, { useState, useEffect  } from 'react';
import './App.css';
import Header from './Header';
import axios from "axios";

function App() {
    const URL_CLIENTS = "http://localhost:8000/votacao/api/questions/"; // (1)
    const [clientList, setClientList] = useState([]); // (2)
    const getClients = () => { // (3)
        axios.get(URL_CLIENTS).then( (request) => {setClientList(request.data)});
    };
    useEffect( () => { //(4)
        getClients();
    }, []);

    return (
        <>
            <Header/>
            <Content/>
        </>
    );
}

function Content() {
    const [gameOver, setGameOver] = useState(false);
    const [game, setGame] = useState({
        database: [],
        currentRow: 1,
        currentLetterPosition: 1,
        currentGuess: '',
        rightGuess: ''
    });

    // Function to handle key press event
    const handleKeyPress = (pressedKey) => {
        // Your logic for handling key press event goes here
    };

    // Function to reset the game
    const resetGame = () => {
        setGame({
            ...game,
            currentRow: 1,
            currentLetterPosition: 1,
            currentGuess: '',
            rightGuess: getOneRandomWord(game.database)
        });
        setGameOver(false);
    };

    // Function to load words from the database
    const loadWords = async () => {
        try {
            const response = await fetch('/static/words.json');
            const { words } = await response.json();
            return words;
        } catch (error) {
            console.error('Error loading words:', error);
            return [];
        }
    };

    // Function to get a random word from the database
    const getOneRandomWord = (wordsList) => {
        const countWords = wordsList.length;
        const shuffleIndex = Math.floor(Math.random() * countWords);
        return wordsList[shuffleIndex].toLowerCase();
    };

    // Function to start the game
    const startGame = async () => {
        const database = await loadWords();
        const rightGuess = getOneRandomWord(database);
        setGame({ ...game, database, rightGuess });
    };

    // Call startGame when component mounts
    useEffect(() => {
        startGame();
    }, []);

    return (
        <main>
            <section className="board-game">
                <div className="row row-1">
                    <div className="letter letter-1"></div>
                    <div className="letter letter-2"></div>
                    <div className="letter letter-3"></div>
                    <div className="letter letter-4"></div>
                    <div className="letter letter-5"></div>
                </div>
                <div className="row row-2">
                    <div className="letter letter-1"></div>
                    <div className="letter letter-2"></div>
                    <div className="letter letter-3"></div>
                    <div className="letter letter-4"></div>
                    <div className="letter letter-5"></div>
                </div>
                <div className="row row-3">
                    <div className="letter letter-1"></div>
                    <div className="letter letter-2"></div>
                    <div className="letter letter-3"></div>
                    <div className="letter letter-4"></div>
                    <div className="letter letter-5"></div>
                </div>
                <div className="row row-4">
                    <div className="letter letter-1"></div>
                    <div className="letter letter-2"></div>
                    <div className="letter letter-3"></div>
                    <div className="letter letter-4"></div>
                    <div className="letter letter-5"></div>
                </div>
                <div className="row row-5">
                    <div className="letter letter-1"></div>
                    <div className="letter letter-2"></div>
                    <div className="letter letter-3"></div>
                    <div className="letter letter-4"></div>
                    <div className="letter letter-5"></div>
                </div>
                <div className="row row-6">
                    <div className="letter letter-1"></div>
                    <div className="letter letter-2"></div>
                    <div className="letter letter-3"></div>
                    <div className="letter letter-4"></div>
                    <div className="letter letter-5"></div>
                </div>
            </section>
            <section className="keyboard">
                <div className="row row-1">
                    <button type="button" className="letter letter-q" value="q">Q</button>
                    <button type="button" className="letter letter-w" value="w">W</button>
                    <button type="button" className="letter letter-e" value="e">E</button>
                    <button type="button" className="letter letter-r" value="r">R</button>
                    <button type="button" className="letter letter-t" value="t">T</button>
                    <button type="button" className="letter letter-y" value="y">Y</button>
                    <button type="button" className="letter letter-u" value="u">U</button>
                    <button type="button" className="letter letter-i" value="i">I</button>
                    <button type="button" className="letter letter-o" value="o">O</button>
                    <button type="button" className="letter letter-p" value="p">P</button>
                </div>

                <div className="row row-2">
                    <button type="button" className="letter letter-a" value="a">A</button>
                    <button type="button" className="letter letter-s" value="s">S</button>
                    <button type="button" className="letter letter-d" value="d">D</button>
                    <button type="button" className="letter letter-f" value="f">F</button>
                    <button type="button" className="letter letter-g" value="g">G</button>
                    <button type="button" className="letter letter-h" value="h">H</button>
                    <button type="button" className="letter letter-j" value="j">J</button>
                    <button type="button" className="letter letter-k" value="k">K</button>
                    <button type="button" className="letter letter-l" value="l">L</button>
                </div>

                <div className="row row-3">
                    <button type="button" className="action enter">ENTER</button>
                    <button type="button" className="letter letter-z" value="z">Z</button>
                    <button type="button" className="letter letter-x" value="x">X</button>
                    <button type="button" className="letter letter-c" value="c">C</button>
                    <button type="button" className="letter letter-v" value="v">V</button>
                    <button type="button" className="letter letter-b" value="b">B</button>
                    <button type="button" className="letter letter-n" value="n">N</button>
                    <button type="button" className="letter letter-m" value="m">M</button>
                    <button type="button" className="action erase" value="⌫">⌫</button>
                </div>
            </section>
            <br/>
            <section className="play-again">
                <button className="btn" type="submit" style={{textAlign: 'center'}}>JOGAR NOVAMENTE</button>
            </section>
            <br/>
        </main>
    );
}

export default App;