// splide slidebar

document.addEventListener( 'DOMContentLoaded', function () {
	new Splide( '#image-slider' ).mount();
} );


const game1 = document.querySelector('.game1');
const game1aktif = document.querySelector('.game1-aktif');
const game1kelar = document.querySelector('.game1-kelar');
const logogame1 = document.querySelector(".logogame1");

const game2 = document.querySelector('.game2');
const game2aktif = document.querySelector('.game2-aktif');
const game2kelar = document.querySelector('.game2-kelar');
const logogame2 = document.querySelector('.logogame2');

const game3 = document.querySelector('.game3');
const game3aktif = document.querySelector('.game3-aktif');
const game3kelar = document.querySelector('.game3-kelar');
const logogame3 = document.querySelector('.logogame3'); 

const tombolactive = document.querySelector('.tombolaktif');
const tombolselesai = document.querySelector('.tombolselesai');


tombolactive.addEventListener('click', function() {
	game1aktif.classList.remove('pembatas-2');
	game1kelar.classList.add('pembatas-2');
	game2aktif.classList.remove('pembatas-2');
	game2kelar.classList.add('pembatas-2');
	game3aktif.classList.remove('pembatas-2');
	game3kelar.classList.add('pembatas-2');
	tombolactive.style.borderRadius = "10px" ;
	tombolactive.style.background = " #5600E7" ;
	tombolselesai.style.background = " #17161A" ;
	tombolselesai.style.borderRadius = "0px 10px 10px 0px" ;
});

tombolselesai.addEventListener('click', function() {
	game1aktif.classList.add('pembatas-2');
	game1kelar.classList.remove('pembatas-2');
	game2aktif.classList.add('pembatas-2');
	game2kelar.classList.remove('pembatas-2');
	game3aktif.classList.add('pembatas-2');
	game3kelar.classList.remove('pembatas-2');
	tombolselesai.style.borderRadius = "10px" ;
	tombolselesai.style.background = " #5600E7" ;
	tombolactive.style.background = " #17161A" ;
	tombolactive.style.borderRadius = "10px 0px 0px 10px" ;
});

logogame1.addEventListener('click',function(){
	game1.classList.remove('pembatas-1');
	game2.classList.add('pembatas-1');
	game3.classList.add('pembatas-1');
	logogame1.style.background = "#5600E7" ;
	logogame2.style.background = "black" ;
	logogame3.style.background = "black" ;
});

logogame2.addEventListener('click',function(){
	game1.classList.add('pembatas-1');
	game2.classList.remove('pembatas-1');
	game3.classList.add('pembatas-1');
	logogame1.style.background = "black" ;
	logogame2.style.background = "#5600E7" ;
	logogame3.style.background = "black" ;
});

logogame3.addEventListener('click',function(){
	game1.classList.add('pembatas-1');
	game2.classList.add('pembatas-1');
	game3.classList.remove('pembatas-1');
	logogame1.style.background = "black" ;
	logogame2.style.background = "black" ;
	logogame3.style.background = "#5600E7" ;
});