import React, { useState } from 'react';

const RockPaperScissors = () => {
  const [gameMode, setGameMode] = useState('menu'); // 'menu', 'player', 'computer'
  const [player1Choice, setPlayer1Choice] = useState('');
  const [player2Choice, setPlayer2Choice] = useState('');
  const [computerChoice, setComputerChoice] = useState('');
  const [player1Score, setPlayer1Score] = useState(0);
  const [player2Score, setPlayer2Score] = useState(0);
  const [computerScore, setComputerScore] = useState(0);
  const [playerScore, setPlayerScore] = useState(0);
  const [gameResult, setGameResult] = useState('');
  const [showResult, setShowResult] = useState(false);
  const [currentPlayer, setCurrentPlayer] = useState(1);

  const choices = [
    { name: 'rock', emoji: '🪨', label: 'Rock' },
    { name: 'paper', emoji: '📄', label: 'Paper' },
    { name: 'scissors', emoji: '✂️', label: 'Scissors' }
  ];

  const getWinner = (choice1, choice2) => {
    if (choice1 === choice2) return 'tie';
    if (
      (choice1 === 'rock' && choice2 === 'scissors') ||
      (choice1 === 'paper' && choice2 === 'rock') ||
      (choice1 === 'scissors' && choice2 === 'paper')
    ) {
      return 'player1';
    }
    return 'player2';
  };

  const getComputerChoice = () => {
    const randomIndex = Math.floor(Math.random() * choices.length);
    return choices[randomIndex].name;
  };

  const handlePlayerChoice = (choice) => {
    if (gameMode === 'player') {
      if (currentPlayer === 1) {
        setPlayer1Choice(choice);
        setCurrentPlayer(2);
      } else {
        setPlayer2Choice(choice);
        const winner = getWinner(player1Choice, choice);
        
        let result = '';
        if (winner === 'tie') {
          result = "It's a tie!";
        } else if (winner === 'player1') {
          result = 'Player 1 wins!';
          setPlayer1Score(prev => prev + 1);
        } else {
          result = 'Player 2 wins!';
          setPlayer2Score(prev => prev + 1);
        }
        
        setGameResult(result);
        setShowResult(true);
        setCurrentPlayer(1);
      }
    } else if (gameMode === 'computer') {
      const compChoice = getComputerChoice();
      setComputerChoice(compChoice);
      setPlayer1Choice(choice);
      
      const winner = getWinner(choice, compChoice);
      
      let result = '';
      if (winner === 'tie') {
        result = "It's a tie!";
      } else if (winner === 'player1') {
        result = 'You win!';
        setPlayerScore(prev => prev + 1);
      } else {
        result = 'Computer wins!';
        setComputerScore(prev => prev + 1);
      }
      
      setGameResult(result);
      setShowResult(true);
    }
  };

  const resetGame = () => {
    setPlayer1Choice('');
    setPlayer2Choice('');
    setComputerChoice('');
    setGameResult('');
    setShowResult(false);
    setCurrentPlayer(1);
  };

  const resetScores = () => {
    setPlayer1Score(0);
    setPlayer2Score(0);
    setComputerScore(0);
    setPlayerScore(0);
    resetGame();
  };

  const backToMenu = () => {
    setGameMode('menu');
    resetScores();
  };

  if (gameMode === 'menu') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-400 via-purple-500 to-pink-500 flex items-center justify-center">
        <div className="bg-white rounded-3xl shadow-2xl p-12 text-center max-w-md w-full mx-4">
          <h1 className="text-4xl font-bold text-gray-800 mb-8">
            🪨📄✂️
          </h1>
          <h2 className="text-3xl font-bold text-gray-700 mb-8">
            Rock Paper Scissors
          </h2>
          <div className="space-y-4">
            <button
              onClick={() => setGameMode('player')}
              className="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-4 px-6 rounded-xl transition-all transform hover:scale-105 shadow-lg"
            >
              👥 2 Players
            </button>
            <button
              onClick={() => setGameMode('computer')}
              className="w-full bg-purple-500 hover:bg-purple-600 text-white font-bold py-4 px-6 rounded-xl transition-all transform hover:scale-105 shadow-lg"
            >
              🤖 vs Computer
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-400 via-purple-500 to-pink-500 p-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-2xl shadow-xl p-6 mb-6">
          <div className="flex justify-between items-center">
            <button
              onClick={backToMenu}
              className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-lg transition-colors"
            >
              ← Menu
            </button>
            <h1 className="text-2xl font-bold text-gray-800">
              {gameMode === 'player' ? '2 Player Mode' : 'vs Computer'}
            </h1>
            <button
              onClick={resetScores}
              className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg transition-colors"
            >
              Reset Scores
            </button>
          </div>
        </div>

        {/* Scores */}
        <div className="bg-white rounded-2xl shadow-xl p-6 mb-6">
          <div className="flex justify-around text-center">
            {gameMode === 'player' ? (
              <>
                <div>
                  <h3 className="text-lg font-bold text-blue-600">Player 1</h3>
                  <p className="text-3xl font-bold">{player1Score}</p>
                </div>
                <div>
                  <h3 className="text-lg font-bold text-red-600">Player 2</h3>
                  <p className="text-3xl font-bold">{player2Score}</p>
                </div>
              </>
            ) : (
              <>
                <div>
                  <h3 className="text-lg font-bold text-blue-600">You</h3>
                  <p className="text-3xl font-bold">{playerScore}</p>
                </div>
                <div>
                  <h3 className="text-lg font-bold text-red-600">Computer</h3>
                  <p className="text-3xl font-bold">{computerScore}</p>
                </div>
              </>
            )}
          </div>
        </div>

        {/* Game Area */}
        <div className="bg-white rounded-2xl shadow-xl p-8">
          {showResult ? (
            <div className="text-center space-y-6">
              <div className="flex justify-center items-center space-x-8 mb-6">
                <div className="text-center">
                  <p className="text-lg font-semibold mb-2">
                    {gameMode === 'player' ? 'Player 1' : 'You'}
                  </p>
                  <div className="text-6xl">{choices.find(c => c.name === player1Choice)?.emoji}</div>
                  <p className="text-sm mt-2">{choices.find(c => c.name === player1Choice)?.label}</p>
                </div>
                
                <div className="text-4xl">VS</div>
                
                <div className="text-center">
                  <p className="text-lg font-semibold mb-2">
                    {gameMode === 'player' ? 'Player 2' : 'Computer'}
                  </p>
                  <div className="text-6xl">
                    {choices.find(c => c.name === (gameMode === 'player' ? player2Choice : computerChoice))?.emoji}
                  </div>
                  <p className="text-sm mt-2">
                    {choices.find(c => c.name === (gameMode === 'player' ? player2Choice : computerChoice))?.label}
                  </p>
                </div>
              </div>
              
              <h2 className="text-3xl font-bold text-gray-800">{gameResult}</h2>
              
              <button
                onClick={resetGame}
                className="bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-8 rounded-xl transition-all transform hover:scale-105"
              >
                Play Again
              </button>
            </div>
          ) : (
            <div className="text-center space-y-6">
              <h2 className="text-2xl font-bold text-gray-800">
                {gameMode === 'player' && currentPlayer === 1 && !player1Choice && 'Player 1, make your choice!'}
                {gameMode === 'player' && currentPlayer === 1 && player1Choice && 'Waiting for Player 1...'}
                {gameMode === 'player' && currentPlayer === 2 && 'Player 2, make your choice!'}
                {gameMode === 'computer' && 'Choose your weapon!'}
              </h2>
              
              {gameMode === 'player' && currentPlayer === 1 && player1Choice && (
                <div className="text-center mb-6">
                  <p className="text-lg text-gray-600">Player 1 has chosen</p>
                  <div className="text-4xl mt-2">❓</div>
                </div>
              )}
              
              <div className="grid grid-cols-3 gap-6 max-w-lg mx-auto">
                {choices.map((choice) => (
                  <button
                    key={choice.name}
                    onClick={() => handlePlayerChoice(choice.name)}
                    className="bg-gray-100 hover:bg-gray-200 rounded-2xl p-6 transition-all transform hover:scale-105 shadow-lg"
                  >
                    <div className="text-5xl mb-2">{choice.emoji}</div>
                    <p className="text-lg font-semibold text-gray-700">{choice.label}</p>
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default RockPaperScissors;
