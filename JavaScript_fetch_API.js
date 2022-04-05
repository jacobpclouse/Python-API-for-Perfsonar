// Learn Fetch API in 6 min
// https://www.youtube.com/watch?v=cuEtnrL9-H0
// Article:
// https://blog.webdevsimplified.com/2022-01/js-fetch-api/


// API I am using to test this with: D&D 5th Edition
// https://www.dnd5eapi.co/api/
// https://www.dnd5eapi.co/api/spells/acid-arrow

// Error I ran into: 
// https://search.brave.com/search?q=VM20%3A1+Uncaught+(in+promise)+TypeError%3A+Failed+to+fetch+at+%3Canonymous%3E%3A1%3A1&source=desktop

fetch('https://regres.in/api/users')
    .then(res => res.json())
    .then(data => console.log(data))