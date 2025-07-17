document.addEventListener('DOMContentLoaded', function() {
  // Elements DOM
  const authContainer = document.querySelector('.auth-container');
  const form = document.querySelector('.auth-form');
  const progressBar = document.getElementById('password-strength-bar');
  const progressPercentage = document.querySelector('.progress-percentage');
  const requiredInputs = document.querySelectorAll('input[required]');
  const createAccountBtn = document.querySelector('.create-account-btn');

  // Animation d'entrée
  if (authContainer) {
    setTimeout(() => {
      authContainer.style.opacity = '1';
      authContainer.style.transform = 'translateY(0)';
    }, 50);
  }

  // Gestion de la force du mot de passe
  function checkPasswordStrength(password) {
    let strength = 0;
    if (password.length > 0) strength += 20;
    if (password.length > 5) strength += 20;
    if (/[A-Z]/.test(password)) strength += 20;
    if (/[0-9]/.test(password)) strength += 20;
    if (/[^A-Za-z0-9]/.test(password)) strength += 20;
    return Math.min(strength, 100);
  }

  // Mise à jour de la progression du formulaire
  function updateFormProgress() {
    const filledCount = Array.from(requiredInputs).filter(i => i.value.trim() !== '').length;
    const progress = (filledCount / requiredInputs.length) * 100;
    document.documentElement.style.setProperty('--form-progress', ${progress}%);
  }

  // Écouteurs d'événements
  if (form) {
    form.addEventListener('submit', function(e) {
      const submitBtn = this.querySelector('button[type="submit"]');
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Traitement...';
      submitBtn.disabled = true;
    });

    const passwordInput = document.getElementById('id_password1');
    if (passwordInput) {
      passwordInput.addEventListener('input', function() {
        const strength = checkPasswordStrength(this.value);
        if (progressBar) progressBar.style.width = ${strength}%;
        if (progressPercentage) progressPercentage.textContent = ${strength}%;
        
        // Changement de couleur
        if (strength < 40) {
          progressBar.style.background = '#e74c3c';
        } else if (strength < 70) {
          progressBar.style.background = '#f39c12';
        } else {
          progressBar.style.background = 'linear-gradient(90deg, var(--primary), var(--primary-dark))';
        }
      });
    }
  }

  // Transition entre pages
  if (createAccountBtn) {
    createAccountBtn.addEventListener('click', function(e) {
      if (this.href) {
        e.preventDefault();
        const overlay = document.createElement('div');
        overlay.className = 'auth-transition-overlay active';
        document.body.appendChild(overlay);
        
        setTimeout(() => {
          window.location.href = this.href;
        }, 600);
      }
    });
  }

  // Validation en temps réel
  requiredInputs.forEach(input => {
    input.addEventListener('input', function() {
      updateFormProgress();
      const parent = this.closest('.form-group');
      
      if (this.value.trim() !== '') {
        parent.classList.add('filled');
        parent.classList.remove('invalid');
        
        if (this.checkValidity()) {
          parent.classList.add('valid');
        }
      } else {
        parent.classList.remove('filled', 'valid');
      }
    });
  });
});