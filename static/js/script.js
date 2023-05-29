function submitb(){

}
        const header = document.querySelector("header");
window.addEventListener("scroll",function(){
    header.classList.toggle("sticky",window.scrollY>100);
});

function checkTextarea() {
  const textarea = document.getElementById('msg');
  const message = textarea.value;
  const wordCount = message.trim().split(/\s+/).length;
  const maxWords = 200;

  if (wordCount > maxWords) {
    const words = message.trim().split(/\s+/).slice(0, maxWords).join(' ');
    textarea.value = words;
  }

  const wordCountSpan = document.getElementById('word-count');
  wordCountSpan.textContent = `${wordCount} words`;
};


Let menu= document.querySelector('#menu-icon');
Let navlist= document.querySelector('.navlist');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navlist.classList.toggle('open');

};

window.onscroll = () => {
    menu.classList.remove('bx-x');
    navlist.classList.remove('open');

};
