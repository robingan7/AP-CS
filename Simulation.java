package PPs;

public class Simulation {
	public static void main(String[]args) {
		final double DELTA_T = 0.01;
		final int INTIAL_V=100;
		double v=100;
		double s=0;
		double g=9.81;
		double time=0;
		int count=0;
		while(v>=0) {
			
				s = s + v * DELTA_T;
				v = v - g * DELTA_T;
				time+=DELTA_T;
				count++;
				if(count%100==0)
					System.out.println("The position is "+s+"\nThe formula is "+(-0.5*g*time*time+INTIAL_V*time)+"\n");
		
		}
	}

}
