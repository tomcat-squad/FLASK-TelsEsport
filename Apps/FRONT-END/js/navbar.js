const toggle = document.querySelector('.toggle input');
const nav = document.querySelector('nav ul');

toggle.addEventListener('change', function(event){
if(this.checked){
    nav.classList.add('slide');
}else{
    nav.classList.remove('slide');
}
})