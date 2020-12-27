const mlinput = document.querySelector('.mobile-legend input');
const ml = document.querySelector('.mobile-legend img');
const pubginput = document.querySelector('.pubg input');
const pubg = document.querySelector('.pubg img');
const pbinput = document.querySelector('.pb input');
const pb = document.querySelector('.pb img');
const mltable = document.querySelector('.ml-tabel');
const pubgtable = document.querySelector('.pubg-tabel');
const pbtable = document.querySelector('.pb-tabel');


ml.addEventListener('click',function(){
    ml.style.background =  " #5600E7 " ;
    pb.style.background =  " #0F0F0F " ;
    pubg.style.background =  " #0F0F0F " ;
    mltable.classList.remove('tabel-hilang') ;
    pubgtable.classList.add('tabel-hilang');
    pbtable.classList.add('tabel-hilang');
})

pubg.addEventListener('click',function(){
    pubg.style.background =  " #5600E7 " ;
    pb.style.background =  " #0F0F0F " ;
    ml.style.background =  " #0F0F0F " ;
    mltable.classList.add('tabel-hilang') ;
    pubgtable.classList.remove('tabel-hilang') ;
    pbtable.classList.add('tabel-hilang') ;
})

pb.addEventListener('click',function(){
    pb.style.background =  " #5600E7 " ;
    ml.style.background =  " #0F0F0F " ;
    pubg.style.background =  " #0F0F0F " ;
    mltable.classList.add('tabel-hilang') ;
    pubgtable.classList.add('tabel-hilang');
    pbtable.classList.remove('tabel-hilang');
})