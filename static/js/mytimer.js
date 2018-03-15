// запустить обратный таймер: initializeClock('clockdiv', 45);

function initializeClock(id, interval_minutes, new_test) {
    var clock = document.getElementById(id);
    var end_time;

    if(new_test) {
        end_time = new Date();
        end_time.setMinutes(end_time.getMinutes() + interval_minutes);
        localStorage.setItem('test_time', JSON.stringify(end_time));
    }
    else {
        end_time = JSON.parse(localStorage.getItem('test_time'));
    }

    function updateClock() {
        var t = getTimeRemaining(end_time);
        clock.innerHTML = ('0' + t.minutes).slice(-2) + ':' + ('0' + t.seconds).slice(-2);

        if(t.minutes < 16) { clock.style.color = 'red'; }
        else if (t.minutes < 31) { clock.style.color = 'blue'; }
        else { clock.style.color = 'green'; }

        if (t.total <= 0) {
            clearInterval(timeinterval);
            time_is_over();
        }
    }

    updateClock(); // запустить функцию один раз, чтобы избежать задержки
    var timeinterval = setInterval(updateClock,1000);
}

function getTimeRemaining(endtime){
    var t = Date.parse(endtime) - Date.parse(new Date());
    var seconds = Math.floor( (t/1000) % 60 );
    var minutes = Math.floor( (t/1000/60) % 60 );
    var hours = Math.floor( (t/(1000*60*60)) % 24 );
    var days = Math.floor( t/(1000*60*60*24) );

    return {
        'total': t,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    };
}

// function time_is_over() {
//     console.log('time is over!!!');
//
// }