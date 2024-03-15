/*
This script contains the logic for a simple coin catcher game.
Coins of different denominations drop from the top of the screen,
and the player must move the catcher left or right to catch the coins.
The game lasts for 15 seconds, after which the player's score is displayed.
*/
// Game variables
const coinContainer = document.getElementById('coin-container');
const catcher = document.getElementById('catcher');
const scoreBoard = document.getElementById('score');
const startButton = document.getElementById('start-button');
let score = 0;
let gameInterval;
let coinInterval;
// Coin denominations
const coinDenominations = [1, 10, 100];
// Start the game
function startGame() {
    startButton.style.display = 'none'; // Hide the start button
    gameInterval = setTimeout(endGame, 15000); // End game after 15 seconds
    coinInterval = setInterval(dropCoin, 1000); // Drop a coin every second
    document.addEventListener('keydown', moveCatcher);
}
// End the game
function endGame() {
    clearInterval(coinInterval);
    document.removeEventListener('keydown', moveCatcher);
    alert(`Game over! Your score is ${score}`);
}
// Drop a coin
function dropCoin() {
    const coin = document.createElement('div');
    coin.classList.add('coin');
    const denomination = coinDenominations[Math.floor(Math.random() * coinDenominations.length)];
    coin.classList.add(`coin-${denomination}`); // Add class based on denomination
    coin.textContent = denomination;
    coin.style.left = `${Math.floor(Math.random() * (coinContainer.clientWidth - 30))}px`; // Random horizontal position
    coinContainer.appendChild(coin);
    // Animate coin dropping
    let position = 0;
    const fallInterval = setInterval(() => {
        position += 5;
        coin.style.top = `${position}px`;
        if (position > coinContainer.clientHeight) {
            clearInterval(fallInterval);
            coinContainer.removeChild(coin);
        }
        checkCollision(coin, denomination, fallInterval);
    }, 50);
}
// Move the catcher
function moveCatcher(event) {
    const leftArrow = 37;
    const rightArrow = 39;
    const step = 20;
    const catcherRect = catcher.getBoundingClientRect();
    const containerRect = coinContainer.getBoundingClientRect();
    if (event.keyCode === leftArrow && catcherRect.left > containerRect.left) {
        catcher.style.left = `${catcher.offsetLeft - step}px`;
    } else if (event.keyCode === rightArrow && catcherRect.right < containerRect.right) {
        catcher.style.left = `${catcher.offsetLeft + step}px`;
    }
}
// Check for collision between coin and catcher
function checkCollision(coin, denomination, fallInterval) {
    const coinRect = coin.getBoundingClientRect();
    const catcherRect = catcher.getBoundingClientRect();
    if (coinRect.bottom >= catcherRect.top &&
        coinRect.top <= catcherRect.bottom &&
        coinRect.right >= catcherRect.left &&
        coinRect.left <= catcherRect.right) {
        clearInterval(fallInterval);
        coinContainer.removeChild(coin);
        updateScore(denomination);
    }
}
// Update the score
function updateScore(denomination) {
    score += denomination;
    scoreBoard.textContent = score;
}
// Add an event listener to the "Start Game" button
startButton.addEventListener('click', startGame);