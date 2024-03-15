<!DOCTYPE html>
<html>
<head>
  <title>Coin Catcher</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      background-color: black;
      font-family: Arial, sans-serif;
    }
    #game-container {
      position: relative;
      width: 400px;
      height: 600px;
      margin: 0 auto;
    }
    #container {
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translate(-50%, 0);
      width: 100px;
      height: 20px;
      background-color: white;
    }
    .coin {
      position: absolute;
      width: 20px;
      height: 20px;
      background-color: yellow;
    }
    #score {
      position: absolute;
      top: 10px;
      left: 10px;
      color: white;
    }
    #time-left {
      position: absolute;
      top: 30px;
      left: 10px;
      color: white;
    }
    #game-over {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: white;
      font-size: 30px;
    }
  </style>
</head>
<body>
  <div id="game-container">
    <div id="container"></div>
    <div id="score">Score: 0</div>
    <div id="time-left">Time Left: 15</div>
    <div id="game-over" style="display: none;">Game Over</div>
  </div>
  <script>
    const container = document.getElementById("container");
    const scoreElement = document.getElementById("score");
    const timeLeftElement = document.getElementById("time-left");
    const gameOverElement = document.getElementById("game-over");
    const coins = [];
    let score = 0;
    let timeLeft = 15;
    let gameOver = false;
    function createCoin() {
      const coin = document.createElement("div");
      coin.classList.add("coin");
      coin.style.left = `${Math.random() * 400}px`;
      coin.style.top = "0px";
      coin.value = Math.floor(Math.random() * 3) + 1;
      coins.push(coin);
      document.getElementById("game-container").appendChild(coin);
    }
    function moveCoin() {
      coins.forEach((coin) => {
        const top = parseInt(coin.style.top);
        coin.style.top = `${top + 5}px`;
        if (top > 600) {
          coin.remove();
          coins.splice(coins.indexOf(coin), 1);
        }
      });
    }
    function moveContainer(e) {
      if (e.key === "ArrowLeft" && container.offsetLeft > 0) {
        container.style.left = `${container.offsetLeft - 5}px`;
      } else if (e.key === "ArrowRight" && container.offsetLeft < 400 - container.offsetWidth) {
        container.style.left = `${container.offsetLeft + 5}px`;
      }
    }
    function checkCollision() {
      coins.forEach((coin) => {
        const coinRect = coin.getBoundingClientRect();
        const containerRect = container.getBoundingClientRect();
        if (coinRect.bottom >= containerRect.top && coinRect.top <= containerRect.bottom && coinRect.right >= containerRect.left && coinRect.left <= containerRect.right) {
          coin.remove();
          coins.splice(coins.indexOf(coin), 1);
          score += coin.value;
          scoreElement.textContent = `Score: ${score}`;
        }
      });
    }
    function updateTimer() {
      timeLeft--;
      timeLeftElement.textContent = `Time Left: ${timeLeft}`;
      if (timeLeft === 0) {
        gameOver = true;
        gameOverElement.style.display = "block";
      }
    }
    function gameLoop() {
      if (!gameOver) {
        moveCoin();
        checkCollision();
        updateTimer();
        requestAnimationFrame(gameLoop);
      }
    }
    document.addEventListener("keydown", moveContainer);
    createCoin();
    gameLoop();
  </script>
</body>
</html>