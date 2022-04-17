const name = document.getElementsByName('name')
const password = document.getElementsByName('password')
const form = document.getElementsByName('form')
const errorElement = document.getElementsByID('error')

form.addEventListener('submit', (e) => {
    let messages = []
    

    if(password.value.length <=6){
        messages.push('Password must be more than 6 charecters')
    }
    if(password.value.length > 20){
        messages.push('Password must be less than 20 charecters')
    }

    if(messages.length>0){
        e.preventDefault()
        errorElement.innerText = messages.join(',')
    }
})