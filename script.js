// DOM Elements

const searchInput = document.getElementById("search-input");

const searchBtn = document.getElementById("search-btn");

const mealsContainer = document.getElementById("meals");

const resultHeading = document.getElementById("result-heading");

const mealDetails = document.getElementById("meal-details");

const mealDetailsContent = document.querySelector(".meal-details-content");

const backBtn = document.getElementById("back-btn");

const clearBtn = document.getElementById("clear-btn");

const scrollToTopBtn = document.getElementById("scroll-to-top-btn");

const randomMealBtn = document.getElementById("random-meal-btn");

const categoryContainer = document.getElementById("category-container");

const categoriesGrid = document.getElementById("categories");

// New DOM Elements for Favorite Recipes
const favoriteRecipesSection = document.getElementById("favorite-recipes-section");
const favoriteMealsContainer = document.getElementById("favorite-meals");


// New DOM Elements for Login/Logout

const signupBtn = document.getElementById("signup-btn");

const loginBtn = document.getElementById("login-btn");

const welcomeMessage = document.getElementById("welcome-message");

const logoutBtn = document.getElementById("logout-btn");

const BASE_URL = "https://www.themealdb.com/api/json/v1/1/";

const SEARCH_URL = `${BASE_URL}search.php?s=`;

const LOOKUP_URL = `${BASE_URL}lookup.php?i=`;

const RANDOM_MEAL_URL = `${BASE_URL}random.php`;

const CATEGORIES_URL = `${BASE_URL}categories.php`;

const FILTER_CATEGORY_URL = `${BASE_URL}filter.php?c=`;



// Event Listeners

searchBtn.addEventListener("click", searchMeals);

mealsContainer.addEventListener("click", handleMealClick);

backBtn.addEventListener("click", () => {
  mealDetails.classList.add("hidden");
  mealDetails.classList.remove("show"); // Ensure animation class is removed
  categoryContainer.classList.remove("hidden");
});

randomMealBtn.addEventListener("click", getRandomMeal);

categoriesGrid.addEventListener("click", handleCategoryClick);

// New event listener for favorite buttons within meal cards
mealsContainer.addEventListener("click", toggleFavoriteStatus);
// New event listener for favorite button within meal details
mealDetailsContent.addEventListener("click", toggleFavoriteStatus);
// Event listener for favorite meal cards to display details
favoriteMealsContainer.addEventListener("click", handleMealClick);

searchInput.addEventListener("keypress", (e) => {

  if (e.key === "Enter") searchMeals();

});



searchInput.addEventListener("input", () => {

  if (searchInput.value.trim() !== "") {

    clearBtn.classList.remove("hidden");

  } else {

    clearBtn.classList.add("hidden");

  }

});



clearBtn.addEventListener("click", () => {

  searchInput.value = "";

  clearBtn.classList.add("hidden");

  mealsContainer.innerHTML = "";

  resultHeading.textContent = "";

  mealDetails.classList.add("hidden");

  categoryContainer.classList.remove("hidden"); // Show categories on clear
  favoriteRecipesSection.classList.add("hidden"); // Hide favorites on clear

});



window.addEventListener("scroll", () => {

  if (window.scrollY > 300) { // Show button after scrolling down 300px

    scrollToTopBtn.classList.add("show");

  } else {

    scrollToTopBtn.classList.remove("show");

  }

});



scrollToTopBtn.addEventListener("click", () => {

  window.scrollTo({

    top: 0,

    behavior: "smooth"

  });

});



logoutBtn.addEventListener("click", logoutUser); // Add logout event listener



// Favorite Recipes Functions
function getFavoriteMeals() {
  const favorites = localStorage.getItem("favoriteMeals");
  return favorites ? JSON.parse(favorites) : [];
}

function addFavoriteMeal(mealId) {
  const favorites = getFavoriteMeals();
  if (!favorites.includes(mealId)) {
    favorites.push(mealId);
    localStorage.setItem("favoriteMeals", JSON.stringify(favorites));
    console.log(`Added meal ${mealId} to favorites.`);
  }
}

function removeFavoriteMeal(mealId) {
  let favorites = getFavoriteMeals();
  favorites = favorites.filter(id => id !== mealId);
  localStorage.setItem("favoriteMeals", JSON.stringify(favorites));
  console.log(`Removed meal ${mealId} from favorites.`);
}

// Authentication Functions
function checkLoginStatus() {

    const isLoggedIn = localStorage.getItem("isLoggedIn");

    const loggedInUserEmail = localStorage.getItem("loggedInUserEmail");



    if (isLoggedIn === "true" && loggedInUserEmail) {

        signupBtn.classList.add("hidden");

        loginBtn.classList.add("hidden");

        welcomeMessage.textContent = `Welcome Back, ${loggedInUserEmail.split('@')[0]}!`; // Display user name before @

        welcomeMessage.classList.remove("hidden");

        logoutBtn.classList.remove("hidden");

        // Ensure main content is visible if user is logged in

        document.querySelector(".container").classList.remove("hidden"); // Assuming container has all main content

    } else {

        // If not logged in, redirect to login page

        // Only redirect if not already on login/signup page to prevent loop

        if (!window.location.pathname.includes("login.html") && !window.location.pathname.includes("signup.html")) {

            window.location.href = "login.html";

        }

        // Hide content for non-logged-in users on index.html if they somehow get here

        document.querySelector(".container").classList.add("hidden");

    }

}



function logoutUser() {

    localStorage.removeItem("isLoggedIn");

    localStorage.removeItem("loggedInUserEmail");

    window.location.href = "login.html"; // Redirect to login page after logout

}



async function getRandomMeal() {

  try {

    resultHeading.textContent = `Fetching a random meal...`;

    mealsContainer.innerHTML = "";

    mealDetails.classList.add("hidden"); // Hide meal details on random meal fetch

    categoryContainer.classList.add("hidden"); // Hide categories on random meal fetch

    



    const response = await fetch(RANDOM_MEAL_URL);

    const data = await response.json();



    



    if (data.meals && data.meals.length > 0) {

      resultHeading.textContent = `Here's a random meal for you:`;

      displayMeals(data.meals);

    } else {

      resultHeading.textContent = ``;

      categoryContainer.classList.remove("hidden"); // Show categories on error

    }

  } catch (error) {

    resultHeading.textContent = "";

    mealsContainer.innerHTML = "";

    mealDetails.classList.add("hidden"); // Hide meal details on error

    categoryContainer.classList.remove("hidden"); // Show categories on error

    

  }

}



async function searchMeals() {

  const searchTerm = searchInput.value.trim();

  // handled the edge case

  if (!searchTerm) {

    resultHeading.textContent = ""; // Clear result heading

    mealsContainer.innerHTML = ""; // Clear meals container

    mealDetails.classList.add("hidden"); // Hide meal details on empty search

    categoryContainer.classList.remove("hidden"); // Show categories

    favoriteRecipesSection.classList.remove("hidden"); // Show favorites

    return;

  }

  try {

    resultHeading.textContent = `Searching for "${searchTerm}"...`;

    mealsContainer.innerHTML = "";

    mealDetails.classList.add("hidden"); // Hide meal details on new search

    categoryContainer.classList.add("hidden"); // Hide categories on new search

    favoriteRecipesSection.classList.add("hidden"); // Hide favorites on new search

    

    // fetch meals from API

    // www.themealdb.com/api/json/v1/1/search.php?s=chicken

    const response = await fetch(`${SEARCH_URL}${searchTerm}`);

    const data = await response.json();

    



    if (data.meals === null) {

      // no meals found

      resultHeading.textContent = ``;

      mealsContainer.innerHTML = "";

      categoryContainer.classList.remove("hidden"); // Show categories on no results
      favoriteRecipesSection.classList.remove("hidden"); // Show favorites on no results
    } else {
      resultHeading.textContent = `Search results for "${searchTerm}":`;
      displayMeals(data.meals);
      searchInput.value = "";
      categoryContainer.classList.add("hidden"); // Hide categories on successful search
      favoriteRecipesSection.classList.add("hidden"); // Hide favorites on successful search
    }
  } catch (error) {
    resultHeading.textContent = "";
    mealsContainer.innerHTML = "";
    mealDetails.classList.add("hidden");
    categoryContainer.classList.remove("hidden"); // Show categories on error
    favoriteRecipesSection.classList.remove("hidden"); // Show favorites on error
  }
}



function displayMeals(meals) {
  mealsContainer.innerHTML = "";
  const fragment = document.createDocumentFragment(); // Create a document fragment
  const favoriteMealIds = getFavoriteMeals(); // Get current favorites

  // loop through meals and create a card for each meal
  meals.forEach((meal) => {
    const mealDiv = document.createElement("div");
    mealDiv.classList.add("meal", "fade-in"); // Add fade-in class
    mealDiv.setAttribute("data-meal-id", meal.idMeal);

    const isFavorited = favoriteMealIds.includes(meal.idMeal);
    const heartIconClass = isFavorited ? "fas fa-heart" : "far fa-heart";

    // Generate a random price between 100 and 1000 Rs.
    const dummyPrice = (Math.random() * (900 - 100) + 100).toFixed(2); // Two decimal places

    mealDiv.innerHTML = `
      <img src="${meal.strMealThumb}" alt="${meal.strMeal}">
      <div class="meal-info">
        <h3 class="meal-title">${meal.strMeal}</h3>
        ${meal.strCategory ? `<div class="meal-category">${meal.strCategory}</div>` : ""}
        <div class="meal-price">Rs. ${dummyPrice}</div> <!-- Price placeholder -->
        <button class="favorite-btn ${isFavorited ? 'favorited' : ''}" data-meal-id="${meal.idMeal}">
          <i class="${heartIconClass}"></i> <!-- Outline heart for unfavorited -->
        </button>
      </div>
    `;
    fragment.appendChild(mealDiv); // Append to the fragment
  });
  mealsContainer.appendChild(fragment); // Append the fragment to the DOM once
}



async function handleMealClick(e) {
  // Check if the clicked element or its parent is a favorite button
  const favoriteBtn = e.target.closest(".favorite-btn");
  if (favoriteBtn) {
      // If it's a favorite button, let toggleFavoriteStatus handle it
      return; 
  }

  const mealEl = e.target.closest(".meal");

  if (!mealEl) return;

  const mealId = mealEl.getAttribute("data-meal-id");


  try {
    
    const response = await fetch(`${LOOKUP_URL}${mealId}`);
    const data = await response.json();


    
    if (data.meals && data.meals[0]) {
      const meal = data.meals[0];
      const ingredients = [];
      for (let i = 1; i <= 20; i++) {
        if (meal[`strIngredient${i}`] && meal[`strIngredient${i}`].trim() !== "") {
          ingredients.push({
            ingredient: meal[`strIngredient${i}`],
            measure: meal[`strMeasure${i}`],
          });
        }
      }
      // display meal details
      const isFavorited = getFavoriteMeals().includes(meal.idMeal);
      const heartIconClass = isFavorited ? "fas fa-heart" : "far fa-heart";

      mealDetailsContent.innerHTML = `
           <img src="${meal.strMealThumb}" alt="${meal.strMeal}" class="meal-details-img">
           <h2 class="meal-details-title">${meal.strMeal}</h2>
           <div class="meal-details-category">
             <span>${meal.strCategory || "Uncategorized"}</span>
           </div>
           <button class="favorite-btn details-favorite-btn ${isFavorited ? 'favorited' : ''}" data-meal-id="${meal.idMeal}">
             <i class="${heartIconClass}"></i> ${isFavorited ? 'Saved Recipe' : 'Save Recipe'}
           </button>
           <div class="meal-details-instructions">
             <h3>Instructions</h3>
             <p>${meal.strInstructions}</p>
           </div>
           <div class="meal-details-ingredients">
             <h3>Ingredients</h3>
             <ul class="ingredients-list">
               ${ingredients
                 .map(
                   (item) => `
                 <li><i class="fas fa-check-circle"></i> ${item.measure} ${item.ingredient}</li>
               `
                 )
                 .join("")}
             </ul>
           </div>
         `;
      mealDetails.classList.remove("hidden");
      mealDetails.classList.add("show"); // Add show class for animation
      categoryContainer.classList.add("hidden"); // Hide categories when meal details are shown
      favoriteRecipesSection.classList.add("hidden"); // Hide favorites when meal details are shown
      mealDetails.scrollIntoView({ behavior: "smooth" });
      scrollToTopBtn.classList.remove("show"); // Hide scroll to top when meal details are visible
    }
  } catch (error) {
    console.error("Error fetching recipe details:", error);
    mealDetails.classList.add("hidden"); // Hide meal details on error
    mealDetails.classList.remove("show"); // Ensure animation class is removed on error
    categoryContainer.classList.remove("hidden"); // Show categories on error
    favoriteRecipesSection.classList.remove("hidden"); // Show favorites on error
  }
}



async function fetchCategories() {

  try {

    

    const response = await fetch(CATEGORIES_URL);

    const data = await response.json();



    



    if (data.categories) {

      displayCategories(data.categories);

    } else {

      console.error("No categories found");

      // Optionally display an error message to the user

    }

  } catch (error) {

    console.error("Error fetching categories:", error);

    resultHeading.textContent = "";

    mealsContainer.innerHTML = "";

    categoryContainer.classList.remove("hidden"); // Show categories on error

    

  }

}



function displayCategories(categories) {

  categoriesGrid.innerHTML = "";

  const fragment = document.createDocumentFragment();



  categories.forEach(category => {

    const categoryItem = document.createElement("div");

    categoryItem.classList.add("category-item", "fade-in"); // Add fade-in class

    categoryItem.setAttribute("data-category-name", category.strCategory);

    categoryItem.innerHTML = `

      <img src="${category.strCategoryThumb}" alt="${category.strCategory}">

      <h3>${category.strCategory}</h3>

    `;

    fragment.appendChild(categoryItem);

  });

  categoriesGrid.appendChild(fragment);

}



async function handleCategoryClick(e) {

  const categoryItem = e.target.closest(".category-item");

  if (!categoryItem) return;



  const categoryName = categoryItem.getAttribute("data-category-name");

  try {

    resultHeading.textContent = `Meals in category: "${categoryName}"...`;

    mealsContainer.innerHTML = "";

    mealDetails.classList.add("hidden");

    categoryContainer.classList.add("hidden"); // Hide categories when a category is clicked

    const response = await fetch(`${FILTER_CATEGORY_URL}${categoryName}`);

    const data = await response.json();



    



    if (data.meals) {

      displayMeals(data.meals);

      resultHeading.textContent = `Showing meals for category: "${categoryName}"`;

    } else {

      resultHeading.textContent = "";

      categoryContainer.classList.remove("hidden"); // Show categories if no meals found
      favoriteRecipesSection.classList.remove("hidden"); // Show favorites if no meals found
    }
  } catch (error) {

    console.error("Error fetching meals by category:", error);

    resultHeading.textContent = "";

    mealsContainer.innerHTML = "";

    categoryContainer.classList.remove("hidden"); // Show categories on error
    favoriteRecipesSection.classList.remove("hidden"); // Show favorites on error
  }
}

function toggleFavoriteStatus(e) {
  const favoriteBtn = e.target.closest(".favorite-btn");
  if (!favoriteBtn) return;

  e.stopPropagation(); // Prevent handleMealClick from being triggered

  const mealId = favoriteBtn.getAttribute("data-meal-id");
  const heartIcon = favoriteBtn.querySelector("i.fa-heart");
  const isFavorited = favoriteBtn.classList.contains("favorited");

  if (isFavorited) {
    removeFavoriteMeal(mealId);
    favoriteBtn.classList.remove("favorited");
    heartIcon.classList.remove("fas");
    heartIcon.classList.add("far");
    if (favoriteBtn.classList.contains("details-favorite-btn")) {
      favoriteBtn.innerHTML = `<i class="far fa-heart"></i> Save Recipe`;
    }
  } else {
    addFavoriteMeal(mealId);
    favoriteBtn.classList.add("favorited");
    heartIcon.classList.remove("far");
    heartIcon.classList.add("fas");
    if (favoriteBtn.classList.contains("details-favorite-btn")) {
      favoriteBtn.innerHTML = `<i class="fas fa-heart"></i> Saved Recipe`;
    }
  }
  displayFavoriteMeals(); // Re-render favorites section after change
}

async function displayFavoriteMeals() {
  favoriteMealsContainer.innerHTML = "";
  const favoriteMealIds = getFavoriteMeals();

  if (favoriteMealIds.length === 0) {
    favoriteRecipesSection.classList.add("hidden");
    return;
  }

  favoriteRecipesSection.classList.remove("hidden");
  const fragment = document.createDocumentFragment();

  for (const mealId of favoriteMealIds) {
    try {
      const response = await fetch(`${LOOKUP_URL}${mealId}`);
      const data = await response.json();
      const meal = data.meals[0];

      if (meal) {
        const mealDiv = document.createElement("div");
        mealDiv.classList.add("meal", "fade-in");
        mealDiv.setAttribute("data-meal-id", meal.idMeal);

        const dummyPrice = (Math.random() * (900 - 100) + 100).toFixed(2);

        mealDiv.innerHTML = `
          <img src="${meal.strMealThumb}" alt="${meal.strMeal}">
          <div class="meal-info">
            <h3 class="meal-title">${meal.strMeal}</h3>
            ${meal.strCategory ? `<div class="meal-category">${meal.strCategory}</div>` : ""}
            <div class="meal-price">Rs. ${dummyPrice}</div>
            <button class="favorite-btn favorited" data-meal-id="${meal.idMeal}">
              <i class="fas fa-heart"></i>
            </button>
          </div>
        `;
        fragment.appendChild(mealDiv);
      }
    } catch (error) {
      console.error(`Error fetching favorite meal ${mealId}:`, error);
      // Optionally, remove the invalid ID from localStorage if it consistently fails
    }
  }
  favoriteMealsContainer.appendChild(fragment);
}

// Initialize on page load
window.addEventListener("load", () => {
  checkLoginStatus();
  // Only fetch categories and favorites if not on login/signup page
  if (!window.location.pathname.includes("login.html") && !window.location.pathname.includes("signup.html")) {
    fetchCategories(); // Always fetch categories
    displayFavoriteMeals(); // Always try to display favorites
  }
});
