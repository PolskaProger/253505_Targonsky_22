// Устанавливаем длительность таймера (1 час = 3600000 миллисекунд)
const TIMER_DURATION = 3600000; // 1 час в миллисекундах

// Проверяем, существует ли сохраненное время начала отсчета в localStorage
let startTime = localStorage.getItem('countdownStartTime');

// Если время не сохранено, устанавливаем текущее время как начало отсчета
if (!startTime) {
    startTime = Date.now();
    localStorage.setItem('countdownStartTime', startTime);
} else {
    // Если отсчет уже закончился, сбрасываем время и обновляем отсчет
    const elapsedTime = Date.now() - parseInt(startTime, 10);
    if (elapsedTime > TIMER_DURATION) {
        startTime = Date.now();
        localStorage.setItem('countdownStartTime', startTime);
    }
}

// Функция для обновления таймера
function updateCountdown() {
    const currentTime = Date.now();
    const elapsedTime = currentTime - parseInt(startTime, 10);
    const remainingTime = TIMER_DURATION - elapsedTime;

    if (remainingTime <= 0) {
        document.getElementById('time-left').textContent = "00:00:00";
        localStorage.removeItem('countdownStartTime'); // Удаляем сохраненное время после завершения
        clearInterval(timerInterval); // Останавливаем таймер
    } else {
        // Вычисляем часы, минуты и секунды для оставшегося времени
        const hours = Math.floor((remainingTime / (1000 * 60 * 60)) % 24);
        const minutes = Math.floor((remainingTime / (1000 * 60)) % 60);
        const seconds = Math.floor((remainingTime / 1000) % 60);

        // Форматируем время с ведущими нулями
        document.getElementById('time-left').textContent =
            `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    }
}

// Обновляем таймер каждую секунду
const timerInterval = setInterval(updateCountdown, 1000);

// Запускаем сразу при загрузке страницы
updateCountdown();
