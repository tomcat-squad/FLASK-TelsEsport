// splide slidebar

document.addEventListener( 'DOMContentLoaded', function () {
	new Splide( '#image-slider' ).mount();
} );


const mlportal = document.querySelector('.ml');
const mlaktif = document.querySelector('.aktif-ml');
const mlselesai = document.querySelector('.ml-kelar');
const logoml = document.querySelector(".logoml");
const pubgportal = document.querySelector('.pubg');
const pubgaktif = document.querySelector('.pubg-aktif');
const pubgselesai = document.querySelector('.pubg-kelar');
const logopubg = document.querySelector('.logopubg');
const pbportal = document.querySelector('.pb');
const pbaktif = document.querySelector('.pb-aktif');
const pbselesai = document.querySelector('.pb-selesai');
const pblogo = document.querySelector('.logopb'); 
const tombolactive = document.querySelector('.tombolaktif');
const tombolselesai = document.querySelector('.tombolselesai');


tombolactive.addEventListener('click', function() {
	mlaktif.classList.remove('pembatas-2');
	mlselesai.classList.add('pembatas-2');
	pubgaktif.classList.remove('pembatas-2');
	pubgselesai.classList.add('pembatas-2');
	pbaktif.classList.remove('pembatas-2');
	pbselesai.classList.add('pembatas-2');
	tombolselesai.style.borderRadius = "0px 10px 10px 0px" ;
	tombolactive.style.borderRadius = "10px" ;
	tombolactive.style.background = " #5600E7" ;
	tombolselesai.style.background = " #17161A" ;
});

tombolselesai.addEventListener('click', function() {
	mlaktif.classList.add('pembatas-2');
	mlselesai.classList.remove('pembatas-2');
	pubgaktif.classList.add('pembatas-2');
	pubgselesai.classList.remove('pembatas-2');
	pbaktif.classList.add('pembatas-2');
	pbselesai.classList.remove('pembatas-2');
	tombolselesai.style.borderRadius = "10px" ;
	tombolactive.style.borderRadius = "10px 0px 0px 10px" ;
	tombolselesai.style.background = " #5600E7" ;
	tombolactive.style.background = " #17161A" ;
});

logoml.addEventListener('click',function(){
	pubgportal.classList.add('pembatas-1');
	mlportal.classList.remove('pembatas-1');
	pbportal.classList.add('pembatas-1');
	logoml.style.background = "#5600E7" ;
	logopubg.style.background = "black" ;
	pblogo.style.background = "black" ;
});

logopubg.addEventListener('click',function(){
	pubgportal.classList.remove('pembatas-1');
	mlportal.classList.add('pembatas-1');
	pbportal.classList.add('pembatas-1');
	logopubg.style.background = "#5600E7" ;
	logoml.style.background = "black" ;
	pblogo.style.background = "black" ;
});

pblogo.addEventListener('click',function(){
	pubgportal.classList.add('pembatas-1');
	mlportal.classList.add('pembatas-1');
	pbportal.classList.remove('pembatas-1');
	pblogo.style.background = "#5600E7" ;
	logopubg.style.background = "black" ;
	logoml.style.background = "black" ;
});