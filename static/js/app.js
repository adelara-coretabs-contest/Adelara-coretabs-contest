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
let scrollToMeals = ()=> {
    let meals = document.querySelector('#main');
    downToMeals.scrollIntoView(meals);
    console.log('meals');
}

let toggleForm = (element)=> {
    let form = document.querySelector('.form');
    let ingredients = document.querySelector('#ingredients');
    let mealName = document.querySelector('#meal-name');
    let thisElement = document.querySelector(`#${element}`)
    console.log(form)
    form.classList.toggle('hidden');
    ingredients.classList.toggle('hidden');
    mealName.classList.toggle('hidden');
    if (thisElement.textContent == 'Order now') {
        thisElement.textContent = 'Cancel';
    } else {
        thisElement.textContent = 'Order now'
    }
    console.log(thisElement)
}