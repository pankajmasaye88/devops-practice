import subprocess

def terraform_run(command):
    process= subprocess.run(command,shell=True,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return process.stdout.decode()

directory="C:\\Users\\panka\\OneDrive\\Documents\\Devops\\Python Practice\\terra-automate"
command= f"terraform -chdir={directory} init"
command=f"terraform -chdir={directory} plan"
command=f"terraform -chdir={directory} apply -autoapprove"
command=f"terraform -chdir={directory} destroy"


#print(command)
terraform_run(command)