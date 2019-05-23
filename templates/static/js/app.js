window.addEventListener('load', ()=> {
    let loader = document.querySelector('#loader');
    loader.classList.add('loaded');
    console.log('loaded', loader)
});


let hamburger = document.querySelector('#hamburger-menu');

hamburger.addEventListener('click', () => {
    console.log(hamburger.children[0]);
    hamburger.classList.toggle('close')
});

let downToMeals = document.querySelector('#scroll-down');
downToMeals.addEventListener('click', ()=> {
    let meals = document.querySelector('#main');
    downToMeals.scrollIntoView(meals);
    console.log('meals');
})
