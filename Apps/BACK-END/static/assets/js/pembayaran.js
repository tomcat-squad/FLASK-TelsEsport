const onlinePortal = document.querySelector('.online img');
const onlineJudul = document.querySelector('.online h3')
const offlinePortal = document.querySelector('.cod img');
const tombolKembali = document.querySelector('.container-utama .tombol-balik');
const isiOnline = document.querySelector('.method-pembayaran');
const isioffline = document.querySelector('.isi-offline');
const offlineJudul = document.querySelector('.cod h3');
const offlinefull = document.querySelector('.container-utama .cod');
const mapcod = document.querySelector('.cod2');

onlinePortal.addEventListener('click',function(){
    tombolKembali.classList.remove('tombol-hilang');
    tombolKembali.style.transition = '2s all';
    onlinePortal.classList.add('online-hilang');
    onlineJudul.classList.add('online-hilang');
    offlinePortal.classList.add('online-hilang');
    isiOnline.style.cursor = "arrow";
    isiOnline.classList.remove('online-hilang');
    isioffline.classList.add('online-hilang');
    offlineJudul.classList.add('online-hilang');
    offlinefull.classList.add('online-hilang');
    isiOnline.classList.add('pembayaran');
    ovo.classList.remove('online-hilang');
    ovopayment.classList.remove('online-hilang');
    isiOnline.style.display = "flex" ;
    mapcod.classList.add('online-hilang');
})

tombolKembali.addEventListener('click',function(){
    tombolKembali.classList.toggle('tombol-hilang');
    onlinePortal.classList.toggle('online-hilang');
    onlineJudul.classList.toggle('online-hilang');
    offlinePortal.classList.toggle('online-hilang');
    isiOnline.classList.toggle('online-hilang');
    isiOnline.style.display = "none";
    isioffline.classList.add('online-hilang');
    offlineJudul.classList.toggle('online-hilang');
    isiOnline.classList.toggle('pembayaran');
    ovopayment.classList.add('online-hilang');
    ovo.classList.add('online-hilang');
    gopaypayment.classList.add('online-hilang');
    danapayment.classList.add('online-hilang');
    mapcod.classList.add('online-hilang');
})

offlinePortal.addEventListener('click',function(){
    tombolKembali.classList.remove('tombol-hilang');
    tombolKembali.style.transition = '2s all';
    onlinePortal.classList.add('online-hilang');
    onlineJudul.classList.add('online-hilang');
    offlinePortal.classList.add('online-hilang');
    isiOnline.classList.add('online-hilang');
    isioffline.classList.remove('online-hilang');
    offlineJudul.classList.add('online-hilang');
    isiOnline.classList.remove('pembayaran');
    ovopayment.classList.add('online-hilang');
    ovo.classList.add('online-hilang');
    gopaypayment.classList.add('online-hilang');
    danapayment.classList.add('online-hilang');
    mapcod.classList.remove('online-hilang');
})

const ovopayment = document.querySelector('.pembayaran-ovo');
const ovo = document.querySelector('.ovo img');
const gopaypayment = document.querySelector('.pembayaran-gopay');
const gopay = document.querySelector('.gopay img');
const danapayment = document.querySelector('.pembayaran-dana');
const dana = document.querySelector('.dana img');

ovo.addEventListener('click',function(){
    ovopayment.classList.remove('online-hilang');
    gopaypayment.classList.add('online-hilang');
    danapayment.classList.add('online-hilang');
})

gopay.addEventListener('click',function(){
    gopaypayment.classList.remove('online-hilang');
    ovopayment.classList.add('online-hilang');
    danapayment.classList.add('online-hilang');
})

dana.addEventListener('click',function(){
    gopaypayment.classList.add('online-hilang');
    ovopayment.classList.add('online-hilang');
    danapayment.classList.remove('online-hilang');
})




// if (document.documentElement.clientWidth > 800){

//     onlinePortal.addEventListener('click',function(){
//         onlinefull.style.width = "1000px";
//     });

//     tombolKembali.addEventListener('click',function(){
//         onlinefull.style.width = "500px";
//     })


// }
 
