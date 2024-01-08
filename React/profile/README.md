onClick needs to be on native dom elements: elements with small letters
so we use handleClick to "carry" the function, then in the star.js use onClick to render the function carried over by handleClick
since toggleFavourite() function is in the main App.js, it can still change the state
