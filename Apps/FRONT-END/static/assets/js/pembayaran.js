const onlinePortal = document.querySelector('.online img');
const offlinePortal = document.querySelector('.cod img');
const tombolKembali = document.querySelector('.container-utama .tombol-balik');
const isiOnline = document.querySelector('.method-pembayaran');
const isioffline = document.querySelector('.isi-offline');
const offlinefull = document.querySelector('.container-utama .cod');
const mapcod = document.querySelector('.cod2');
const onlineContainer = document.querySelector('.online');
const offlineContainer = document.querySelector('.cod');
const footer = document.querySelector('footer');

onlinePortal.addEventListener('click',function(){
    tombolKembali.classList.remove('tombol-hilang');
    tombolKembali.style.transition = '2s all';
    onlinePortal.classList.add('online-hilang');
    offlinePortal.classList.add('online-hilang');
    isiOnline.style.cursor = "arrow";
    isiOnline.classList.remove('online-hilang');
    isioffline.classList.add('online-hilang');
    offlinefull.classList.add('online-hilang');
    isiOnline.classList.add('pembayaran');
    // ovo.classList.remove('online-hilang');
    // ovopayment.classList.remove('online-hilang');
    isiOnline.style.display = "flex" ;
    mapcod.classList.add('online-hilang');
    danapayment.style.display = "block" ;
})

tombolKembali.addEventListener('click',function(){
    tombolKembali.classList.toggle('tombol-hilang');
    onlinePortal.classList.toggle('online-hilang');
    offlinePortal.classList.toggle('online-hilang');
    isiOnline.classList.toggle('online-hilang');
    isiOnline.style.display = "none";
    isioffline.classList.add('online-hilang');
    isiOnline.classList.toggle('pembayaran');
    // ovopayment.classList.add('online-hilang');
    // ovo.classList.add('online-hilang');
    // gopaypayment.classList.add('online-hilang');
    danapayment.style.display = "none"; 
    mapcod.classList.add('online-hilang');
})

offlinePortal.addEventListener('click',function(){
    tombolKembali.classList.remove('tombol-hilang');
    tombolKembali.style.transition = '2s all';
    onlinePortal.classList.add('online-hilang');
    offlinePortal.classList.add('online-hilang');
    isiOnline.classList.add('online-hilang');
    isioffline.classList.remove('online-hilang');
    isiOnline.classList.remove('pembayaran');
    // ovopayment.classList.add('online-hilang');
    // ovo.classList.add('online-hilang');
    // gopaypayment.classList.add('online-hilang');
    danapayment.classList.add('online-hilang');
    mapcod.classList.remove('online-hilang');
})

// const ovopayment = document.querySelector('.pembayaran-ovo');
// const ovo = document.querySelector('.ovo img');
// const gopaypayment = document.querySelector('.pembayaran-gopay');
// const gopay = document.querySelector('.gopay img');
const danapayment = document.querySelector('.pembayaran-dana');
const dana = document.querySelector('.dana img');

// ovo.addEventListener('click',function(){
//     ovopayment.classList.remove('online-hilang');
//     // gopaypayment.classList.add('online-hilang');
//     danapayment.classList.add('online-hilang');
// })

// gopay.addEventListener('click',function(){
//     gopaypayment.classList.remove('online-hilang');
//     ovopayment.classList.add('online-hilang');
//     danapayment.classList.add('online-hilang');
// })

dana.addEventListener('click',function(){
    // gopaypayment.classList.add('online-hilang');
    // ovopayment.classList.add('online-hilang');
    danapayment.style.display = "block";
})




// if (document.documentElement.clientWidth > 800){

//     onlinePortal.addEventListener('click',function(){
//         onlinefull.style.width = "1000px";
//     });

//     tombolKembali.addEventListener('click',function(){
//         onlinefull.style.width = "500px";
//     })


// }

if (document.documentElement.clientWidth < 600) {
    tombolKembali.addEventListener('click', function(){
        onlineContainer.style.marginTop = "40px" ;
        footer.style.marginTop = "60px" ;
        offlineContainer.style.marginTop = "30px" ;
        onlineContainer.style.marginBottom = "30px" ;
    });

    onlinePortal.addEventListener('click', function(){
        onlineContainer.style.marginTop = "-10px" ;
        // onlineContainer.style.marginBottom = "1px" ;
        footer.style.marginTop = "190px" ;
        offlineContainer.style.marginTop = "-50px" ;
    });

    offlinePortal.addEventListener('click',function(){ 
        onlineContainer.style.marginBottom = "100px" ;
        onlineContainer.style.marginTop = "20px" ;
        footer.style.marginTop = "130px" ;
    });

} 
