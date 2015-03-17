
import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.xmlrpc.XmlRpcException;
import org.apache.xmlrpc.client.XmlRpcClient;
import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author freddy
 */
public class Vuelos extends javax.swing.JFrame {

    /**
     * Creates new form Vuelos
     */
    public Vuelos() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel3 = new javax.swing.JPanel();
        jTabbedPane1 = new javax.swing.JTabbedPane();
        jPanel1 = new javax.swing.JPanel();
        nombre = new javax.swing.JTextField();
        pais = new javax.swing.JTextField();
        contraseña = new javax.swing.JTextField();
        CrearAero = new javax.swing.JButton();
        jButton1 = new javax.swing.JButton();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel1 = new javax.swing.JLabel();
        jPanel2 = new javax.swing.JPanel();
        jLabel2 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setMinimumSize(new java.awt.Dimension(897, 610));
        setPreferredSize(new java.awt.Dimension(895, 600));
        setResizable(false);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jPanel3.setBackground(new java.awt.Color(0, 0, 0));

        jTabbedPane1.setFont(new java.awt.Font("Arial", 1, 14)); // NOI18N
        jTabbedPane1.setMinimumSize(new java.awt.Dimension(885, 571));
        jTabbedPane1.setPreferredSize(new java.awt.Dimension(885, 571));

        jPanel1.setBackground(new java.awt.Color(255, 51, 51));
        jPanel1.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());
        jPanel1.add(nombre, new org.netbeans.lib.awtextra.AbsoluteConstraints(340, 150, 240, -1));
        jPanel1.add(pais, new org.netbeans.lib.awtextra.AbsoluteConstraints(340, 200, 240, -1));
        jPanel1.add(contraseña, new org.netbeans.lib.awtextra.AbsoluteConstraints(340, 250, 240, -1));

        CrearAero.setBackground(new java.awt.Color(0, 0, 0));
        CrearAero.setFont(new java.awt.Font("Arial", 1, 18)); // NOI18N
        CrearAero.setForeground(new java.awt.Color(255, 255, 255));
        CrearAero.setText("REGISTRAR");
        CrearAero.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                CrearAeroActionPerformed(evt);
            }
        });
        jPanel1.add(CrearAero, new org.netbeans.lib.awtextra.AbsoluteConstraints(630, 450, -1, -1));

        jButton1.setText("jButton1");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });
        jPanel1.add(jButton1, new org.netbeans.lib.awtextra.AbsoluteConstraints(470, 440, -1, -1));

        jLabel3.setBackground(new java.awt.Color(102, 102, 102));
        jLabel3.setFont(new java.awt.Font("Arial", 1, 14)); // NOI18N
        jLabel3.setForeground(new java.awt.Color(204, 0, 0));
        jLabel3.setText("Nombre:");
        jPanel1.add(jLabel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(270, 150, -1, -1));

        jLabel4.setBackground(new java.awt.Color(102, 102, 102));
        jLabel4.setFont(new java.awt.Font("Arial", 1, 14)); // NOI18N
        jLabel4.setForeground(new java.awt.Color(204, 0, 0));
        jLabel4.setText("Pais:");
        jPanel1.add(jLabel4, new org.netbeans.lib.awtextra.AbsoluteConstraints(300, 200, -1, -1));

        jLabel5.setBackground(new java.awt.Color(102, 102, 102));
        jLabel5.setFont(new java.awt.Font("Arial", 1, 14)); // NOI18N
        jLabel5.setForeground(new java.awt.Color(204, 0, 0));
        jLabel5.setText("Contraseña:");
        jPanel1.add(jLabel5, new org.netbeans.lib.awtextra.AbsoluteConstraints(240, 250, -1, -1));

        jLabel1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/aeropuerto.jpg"))); // NOI18N
        jPanel1.add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 880, 540));

        jTabbedPane1.addTab("CREAR AEROPUERTOS", jPanel1);

        jPanel2.setBackground(new java.awt.Color(51, 0, 204));
        jPanel2.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel2.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/vuelos.jpg"))); // NOI18N
        jPanel2.add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 880, 540));

        jTabbedPane1.addTab("CREAR VUELOS", jPanel2);

        javax.swing.GroupLayout jPanel3Layout = new javax.swing.GroupLayout(jPanel3);
        jPanel3.setLayout(jPanel3Layout);
        jPanel3Layout.setHorizontalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel3Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jTabbedPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 880, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(180, Short.MAX_VALUE))
        );
        jPanel3Layout.setVerticalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel3Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jTabbedPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 570, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(29, Short.MAX_VALUE))
        );

        getContentPane().add(jPanel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 1070, 610));

        pack();
    }// </editor-fold>//GEN-END:initComponents
   int contador=0;
    private void CrearAeroActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_CrearAeroActionPerformed
        String nom=nombre.getText().trim();
        String pa=pais.getText().trim();
        String contrase=contraseña.getText().trim();
        
        XmlRpcClient client = null;
        
            try { 
	    // Generar el Cliente 
	   XmlRpcClientConfigImpl config = new XmlRpcClientConfigImpl();
           
           contador++;
           String conta=String.valueOf(contador);
           System.out.println("cont1: "+conta);
           config.setServerURL(new URL("http://localhost:9000"));
           client=new XmlRpcClient();
           client.setConfig(config);
         
           
           
           Object[] parametrosUsuario = new Object[]{conta,nom,pa,contrase};
           String dato=(String) client.execute("ListaAeropuerto",parametrosUsuario);
                System.out.println("datos: "+dato);
          
          
        } catch (XmlRpcException e) { 
	    System.out.println("Error en XML-RPC: " + e.getMessage());
	}   catch (MalformedURLException ex) {
                Logger.getLogger(Vuelos.class.getName()).log(Level.SEVERE, null, ex);
            }
    }//GEN-LAST:event_CrearAeroActionPerformed
    int contador2=0;
    String cont="";
    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
             try { 
            XmlRpcClient client = null;
	    // Generar el Cliente 
	   XmlRpcClientConfigImpl config = new XmlRpcClientConfigImpl();

           contador2+=1;

           config.setServerURL(new URL("http://localhost:9000"));
                    
           client=new XmlRpcClient();
           client.setConfig(config);
         
           
            cont=String.valueOf(contador2);
            System.out.println("contador2: "+cont);
            Object[] params4 = new Object[]{cont};
            String dato2=(String) client.execute("MostrarListaAero",params4);
            System.out.println(dato2);
           
        } catch (XmlRpcException e) { 
	    System.out.println("Error en XML-RPC: " + e.getMessage());
	}   catch (MalformedURLException ex) {
                Logger.getLogger(Vuelos.class.getName()).log(Level.SEVERE, null, ex);
            }
    }//GEN-LAST:event_jButton1ActionPerformed

    /**
     * @param args the command line arguments
     */

    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Vuelos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Vuelos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Vuelos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Vuelos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Vuelos().setVisible(true);
       
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton CrearAero;
    private javax.swing.JTextField contraseña;
    private javax.swing.JButton jButton1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JTabbedPane jTabbedPane1;
    private javax.swing.JTextField nombre;
    private javax.swing.JTextField pais;
    // End of variables declaration//GEN-END:variables
}