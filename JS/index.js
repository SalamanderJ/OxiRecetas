function toggleResetPswd(e){
    e.preventDefault();
    $('#logreg-forms .form-signin').toggle()
    $('#logreg-forms .form-reset').toggle() 
}

function toggleSignUp(e){
    e.preventDefault();
    $('#logreg-forms .form-signin').toggle(); 
    $('#logreg-forms .form-signup').toggle(); 
}

$(()=>{
    // Login Registrar
    $('#logreg-forms #forgot_pswd').click(toggleResetPswd);
    $('#logreg-forms #cancel_reset').click(toggleResetPswd);
    $('#logreg-forms #btn-signup').click(toggleSignUp);
    $('#logreg-forms #cancel_signup').click(toggleSignUp);
})
$(".slides").slidesjs({
        play: {
      active: true,
     
      effect: "fade",
       
      interval: 3000,
     
      auto: true,
       
      swap: true,
       
      pauseOnHover: false,
        
      restartDelay: 2500
       
    }
      });



 




