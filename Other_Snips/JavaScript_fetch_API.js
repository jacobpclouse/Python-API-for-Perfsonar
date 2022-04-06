// Learn Fetch API in 6 min
// https://www.youtube.com/watch?v=cuEtnrL9-H0
// Article:
// https://blog.webdevsimplified.com/2022-01/js-fetch-api/


// API I am using to test this with: D&D 5th Edition
// https://www.dnd5eapi.co/api/
// https://www.dnd5eapi.co/api/spells/acid-arrow

// Error I ran into: 
// https://search.brave.com/search?q=VM20%3A1+Uncaught+(in+promise)+TypeError%3A+Failed+to+fetch+at+%3Canonymous%3E%3A1%3A1&source=desktop

// ----- Useful videos and links -----
// Learn Promises in JS
// https://www.youtube.com/watch?v=DHvZLI7Db8E&t=0s

// Async Await Tutorial
// https://www.youtube.com/watch?v=V_Kr9OSfDeU&t=0s


// -- OLD --
// fetch('https://regres.in/api/users')
//     .then(res => res.json())
//     .then(data => console.log(data))


fetch('https://regres.in/api/users', {
    // Defaults to GET, can remove method, headers and body labels here if you just want to use GET
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        name: 'User 1'
    })
})
    .then(res => {
        // if (res.ok){
        //     console.log('SUCCESS!!')
        // } else {
        //     console.log('Response was not Successfull...')
        // }
        // res.json()
        return res.json()
    })
    .then(data => console.log(data))
