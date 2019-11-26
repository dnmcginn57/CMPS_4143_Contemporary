import java.util.ArrayList;
import java.util.Collections;

public class BankerAlgo{
    public static void main(String[] args) {
        ArrayList<Double> prizes = new ArrayList<Double>();
        prizes.add(10000.0);
        prizes.add(50000.0);
        prizes.add(25000.0);
        double exp = PredictValue(prizes);
        System.out.println(Offer(exp,20,Collections.max(prizes)));
        System.out.println(exp);
                
    }
    /*
    public static double Offer(double,int,double)
    Accepts:
        expected value of player's case
        Number of cases in play arrayList.length()
        Maximum value in play (Collections.max(arrayList))
    Returns:
        Banker's offer as a double
   
     */
    public static double Offer(double Expected, int NumCases, double Maximum){
        double offer = 12275.30;
        offer += (.748*Expected) + (-2714.74 * NumCases) + (-.4*Maximum) + (.0000006986*(Expected*Expected)) + (32.623*(NumCases*NumCases));
        

        return(-1*offer);

    }
    /*
    public static double PredictValue(ArrayList<Double>)
    Accepts:
        Arraylist containing prize values
    Returns:
        Expected value of player's case
    Notes:
        assign returned value to variable and pass to Offer
     */
    public static double PredictValue(ArrayList<Double> prize){
        ArrayList<Double> tmp = new ArrayList<Double>();
        for(double i: prize){
            tmp.add(i);
        }
        Collections.sort(tmp);
        return(tmp.get(tmp.size()/2));
    }
}