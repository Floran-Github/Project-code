class mythread extends Thread{
    public void run(){
        for(int i = 1;i<=5;i++){
            System.out.print("$");
        
            try{
                sleep(1000);
            }
            catch(Exception e){

            }
        }
    }
    
}

class secondtheard extends Thread{
    
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.print("*");
            try{
                sleep(500);
            }
            catch(Exception e){

            }
        }
    }
}
public class javathread {
    public static void main(String[] args) {
        mythread ob = new mythread();
        secondtheard ob2 = new secondtheard();
        ob.start();
        ob2.start();
    }
}