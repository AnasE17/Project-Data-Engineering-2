pipeline{
  agent any
  stages {
  	stage('Build docker image'){
  		steps{
  			script{
  				if (env.BRANCH_ENV != 'master') {
		    		powershell 'docker build -t app .'
		  		}
				}
    	}
    }
    
    stage('Run containerized application'){
      steps{
  			script{
  				if (env.BRANCH_ENV != 'master' ) {
		    		powershell 'docker run -p 5000:5000 app'
		  		}
				}
    	}
    }
		
    stage('Integration and Unit tests '){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'feature' ) {
							powershell 'python test_unit.py'
              powershell 'python test_integration.py'
		    	}
				}
			}
		}
		 stage('stress_test'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'develop') {
      				powershell 'python test_stress.py'
					}
				}
				
		  }
		}
	
    
		
		
	
		
	
		stage('push to release'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'develop') {
    					powershell 'git checkout -b release || git checkout release'	
    					powershell 'git fetch'	
    					powershell 'git pull'
    					powershell 'git merge origin/develop'
    					powershell 'git commit --allow-empty -m "release the application"'
    					powershell 'git push -f https://Kimpouni:codelyoko_93@github.com/AnasE17/Project-Data-Engineering-2.git'
					}
				}
				
		  }
		}
		
		stage('Release phase'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							echo '"deploying"' 
		    	}
				}
			}
		}
		
		stage('User acceptance'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							input 'Accept merge to master ??'
		    	}
				}
			}
		}
		
		stage('Final merging'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							powershell 'git checkout -b main || git checkout main'
							powershell 'git merge origin/release'
							powershell 'git push -f https://Kimpouni:codelyoko_93@github.com/AnasE17/Project-Data-Engineering-2.git'
		    	}
				}
			}
		}
				
				
		stage('Delete container'){
     		steps{
     			script{
     				if (env.BRANCH_NAME != 'master') {
							powershell 'docker rmi -f app'
		    	}
				}
			}
		}
		
		
	}
}
