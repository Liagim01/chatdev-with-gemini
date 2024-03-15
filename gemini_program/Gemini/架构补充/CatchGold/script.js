// Game Constants
const CANVAS_WIDTH = 800;
const CANVAS_HEIGHT = 600;
const CONTAINER_WIDTH = 100;
const CONTAINER_HEIGHT = 20;
const COIN_RADIUS = 10;
const COIN_SPEED = 3;
const COIN_VALUES = [1, 10, 100];
const GAME_DURATION = 3000; // in seconds
// Game Variables
let canvas, ctx;
let containerX, containerY;
let coins = [];
let score = 0;
let gameStarted = false;
let gameTimer;
let gameOverScreen;
let finalScoreElement;
let restartButton;
let countdownElement;
let countdownTimer;
// Initialize the game
function init() {
  canvas = document.getElementById("gameCanvas");
  ctx = canvas.getContext("2d");
  canvas.width = CANVAS_WIDTH;
  canvas.height = CANVAS_HEIGHT;
  containerX = CANVAS_WIDTH / 2 - CONTAINER_WIDTH / 2;
  containerY = CANVAS_HEIGHT - CONTAINER_HEIGHT;
  gameOverScreen = document.getElementById("gameOverScreen");
  finalScoreElement = document.getElementById("finalScore");
  restartButton = document.getElementById("restartButton");
  countdownElement = document.createElement("div");
  countdownElement.id = "countdown";
  document.body.appendChild(countdownElement);
  document.addEventListener("keydown", handleKeyDown);
  document.addEventListener("keyup", handleKeyUp);
  restartButton.addEventListener("click", restartGame);
  startGame();
}
// Start the game
function startGame() {
  gameStarted = true;
  score = 0;
  coins = [];
  countdownTimer = GAME_DURATION;
  gameTimer = setInterval(updateGame, 1000 / 60); // 60 FPS
  countdownElement.innerText = countdownTimer;
  setTimeout(endGame, GAME_DURATION * 1000);
}
// End the game
function endGame() {
  gameStarted = false;
  clearInterval(gameTimer);
  canvas.style.display = "none";
  gameOverScreen.style.display = "block";
  finalScoreElement.innerText = "Final Score: " + score;
}
// Restart the game
function restartGame() {
  canvas.style.display = "block";
  gameOverScreen.style.display = "none";
  init();
}
// Update the game state
function updateGame() {
  clearCanvas();
  updateContainer();
  updateCoins();
  renderContainer();
  renderCoins();
  renderScore();
  updateCountdown();
}
// Clear the canvas
function clearCanvas() {
  ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
}
// Update the container position based on user input
function updateContainer() {
  if (leftKeyPressed) {
    containerX -= 5;
    if (containerX < 0) {
      containerX = 0;
    }
  } else if (rightKeyPressed) {
    containerX += 5;
    if (containerX + CONTAINER_WIDTH > CANVAS_WIDTH) {
      containerX = CANVAS_WIDTH - CONTAINER_WIDTH;
    }
  }
}
// Update the coin positions and check for collisions
function updateCoins() {
  for (let i = 0; i < coins.length; i++) {
    const coin = coins[i];
    coin.y += COIN_SPEED;
    if (coin.y + COIN_RADIUS > CANVAS_HEIGHT) {
      coins.splice(i, 1);
    }
    if (
      coin.x + COIN_RADIUS > containerX &&
      coin.x - COIN_RADIUS < containerX + CONTAINER_WIDTH &&
      coin.y + COIN_RADIUS > containerY &&
      coin.y - COIN_RADIUS < containerY + CONTAINER_HEIGHT
    ) {
      coins.splice(i, 1);
      score += coin.value;
    }
  }
  if (Math.random() < 0.05) {
    const coinValue = COIN_VALUES[Math.floor(Math.random() * COIN_VALUES.length)];
    const coinX = Math.random() * (CANVAS_WIDTH - 2 * COIN_RADIUS) + COIN_RADIUS;
    const coinY = 0;
    coins.push({ x: coinX, y: coinY, value: coinValue });
  }
}
// Render the container
function renderContainer() {
  ctx.fillStyle = "blue";
  ctx.fillRect(containerX, containerY, CONTAINER_WIDTH, CONTAINER_HEIGHT);
}
// Render the coins
function renderCoins() {
  for (let i = 0; i < coins.length; i++) {
    const coin = coins[i];
    ctx.fillStyle = "gold";
    ctx.beginPath();
    ctx.arc(coin.x, coin.y, COIN_RADIUS, 0, 2 * Math.PI);
    ctx.fill();
  }
}
// Render the score
function renderScore() {
  ctx.fillStyle = "black";
  ctx.font = "20px Arial";
  ctx.fillText("Score: " + score, 10, 30);
}
// Update the countdown timer
function updateCountdown() {
  countdownTimer--;
  countdownElement.innerText = countdownTimer;
  if (countdownTimer <= 0) {
    endGame();
  }
}
// Handle keydown events
let leftKeyPressed = false;
let rightKeyPressed = false;
function handleKeyDown(event) {
  if (event.keyCode === 37) {
    leftKeyPressed = true;
  } else if (event.keyCode === 39) {
    rightKeyPressed = true;
  }
}
// Handle keyup events
function handleKeyUp(event) {
  if (event.keyCode === 37) {
    leftKeyPressed = false;
  } else if (event.keyCode === 39) {
    rightKeyPressed = false;
  }
}
// Start the game when the page is loaded
window.onload = init;