const game1 = document.querySelector('.game-1 img');
const game2 = document.querySelector('.game-2 img');
const game3 = document.querySelector('.game-3 img');
const game1table = document.querySelector('.game1-tabel');
const game2table = document.querySelector('.game2-tabel');
const game3table = document.querySelector('.game3-tabel');


game1.addEventListener('click',function(){
    game1.style.background =  " #5600E7 " ;
    game2.style.background =  " #0F0F0F " ;
    game3.style.background =  " #0F0F0F " ;
    game1table.classList.remove('tabel-hilang') ;
    game2table.classList.add('tabel-hilang');
    game3table.classList.add('tabel-hilang');
})

game2.addEventListener('click',function(){
    game1.style.background =  " #0F0F0F " ;
    game2.style.background =  " #5600E7 " ;
    game3.style.background =  " #0F0F0F " ;
    game1table.classList.add('tabel-hilang') ;
    game2table.classList.remove('tabel-hilang') ;
    game3table.classList.add('tabel-hilang') ;
})

game3.addEventListener('click',function(){
    game1.style.background =  " #0F0F0F " ;
    game2.style.background =  " #0F0F0F " ;
    game3.style.background =  " #5600E7 " ;
    game1table.classList.add('tabel-hilang') ;
    game2table.classList.add('tabel-hilang');
    game3table.classList.remove('tabel-hilang');
})