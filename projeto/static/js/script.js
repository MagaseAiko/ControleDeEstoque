document.addEventListener('DOMContentLoaded', function() {
    function updateTime(){
        const now = new Date();

        const year = now.getFullYear();
        const month = (now.getMonth() + 1).toString().padStart(2, '0');
        const day = now.getDate().toString().padStart(2, '0');
        const hours = now.getHours().toString().padStart(2,'0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        const seconds = now.getSeconds().toString().padStart(2, '0');
        const dateString = `${day}/${month}/${year}`;
        const timeString = `${hours}:${minutes}:${seconds}`;
        const dateTimeString = `${dateString} ${timeString}`;
        document.getElementById('clock').textContent = dateTimeString;
    }
    updateTime();
    setInterval(updateTime, 1000);
});

