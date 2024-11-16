let list = document.querySelector('.slider .list');
let items = document.querySelectorAll('.slider .list .item');
let dots = document.querySelectorAll('.slider .dots li');
let prev = document.getElementById('prev');
let next = document.getElementById('next');

let active = 0;
let lengthitems = items.length - 1;

next.onclick = function() {
    if (active + 1 > lengthitems) {
        active = 0;
    } else {
        active = active + 1;
    }
    reloadslider();
}

prev.onclick = function() {
    if (active - 1 < 0) {
        active = lengthitems;
    } else {
        active = active - 1;
    }
    reloadslider();
}

let autoslide = setInterval(() => { next.click(); }, 3000);

function reloadslider() {
    let checkleft = items[active].offsetLeft;
    list.style.left = -checkleft + 'px';

    let lastactiveDot = document.querySelector('.slider .dots li.active');
    if (lastactiveDot) lastactiveDot.classList.remove('active');
    dots[active].classList.add('active');
}

dots.forEach((li, key) => {
    li.addEventListener('click', function() {
        active = key;
        reloadslider();
    })
})

//------------------------------------------------------//

const cardSlider = document.querySelector('.card-slider');
const cards = document.querySelectorAll('.card');
let currentIndex = 1;

document.querySelector('.next-btn').addEventListener('click', () => {
    if (currentIndex < cards.length - 3) {
        currentIndex++;
        updateSlider();
    }
});

document.querySelector('.prev-btn').addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
        updateSlider();
    }
});

function updateSlider() {
    const cardWidth = cards[0].clientWidth + 30; // Card width + gap
    const translateX = -(currentIndex * cardWidth);

    cardSlider.style.transform = `translateX(${translateX}px)`;

    cards.forEach((card, index) => {
        card.classList.remove('active');
        if (index === currentIndex + 1) {
            card.classList.add('active'); // Zoom effect for middle card
        }
    });
}

// Initialize the slider
updateSlider();
//------------------------------------------------------//


var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 2000);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "block";
}


function display() {
   
    document.getElementById("nav_drop").classList.toggle("flex");
}
//------------------------------------------------------//

