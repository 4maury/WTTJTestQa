describe('Create candidate', function() {
  it('Test if the creation of a new candidate works', function() {
  	// The following URL leads to the connexion page
	cy.visit('https://www.welcomekit.co/dashboard/o/dkxzma3/jobs/2XMOI_yq66e6b/new-candidate/392777')
	cy.get('.user_email')
		.type('kevin+wttj-81cc3c987b56af3cf082baea@wttj.co')
	cy.get('.user_password')
		.type('=v%+$a^|d@1_th2')
	cy.pause()
	// Can't pass the Captcha : do it manually while it is paused
	/*cy.get('div.rc-anchor-center-item.rc-anchor-checkbox-holder')
		.click()*/
	cy.get('button.btn.btn-primary')
		.click()
	cy.url().should('include', 'dashboard')
	})
})
