#   Computation of the still water resistance through Holtrop and Mennem approach (1982)

'''
Inspired in F_SWResist.m

'''

class StillWaterResistance():

    def __init__(self, L, B, T_F ,T_A ,nabla ,LCB ,A_BT ,h_B ,C_M ,C_WP ,A_T ,S_APP ,apk2 ,Cstern ,V_S):
        self.L              = L         # length on waterline [m]
        self.B              = B         # breadth moulded [m]
        self.T_F            = T_F       # draught moulded on F.P. [m]
        self.T_A            = T_A       # draught moulded on A.P. [m]
        self.nabla          = nabla     # displacement volume moulded [m^3]
        self.LCB            = LCB       # longitudinal centre of buoyancy [% relative to 1/2L]
        self.A_BT           = A_BT      # transverse bulb area [m^2]
        self.h_B            = h_B       # centre of bulb area above keel line [m]
        self.C_M            = C_M       # midship section coefficient []
        self.C_WP           = C_WP      # waterplane area coefficient []
        self.A_T            = A_T       # transom area [m^2]
        self.S_APP          = S_APP     # wetted area apendages [m^2]
        self.apk2           = apk2      # appendage resistance factor []
        self.Cstern         = Cstern    # stern shape parameter []
        self.V_S            = V_S*1852/3600 # service speed [m/s]
        self.g              = 9.80665       # gravity acceleration [m/s^2]
        self.nu             = 1.1390e-6     # kinematic viscosity of fresh water at 15°C [m^2/s]
        self.rho            = 999           # density of fresh water [kg/m^3]
        self.d              = -0.9
        self.Fn             = self.V_S/(self.g*self.L)^0.5                  # Froud number
        self.Rn             = self.V_S*self.L/self.nu                       # Reynolds number
        self.T_M            = (self.T_A + self.T_F)/2                       # mean draught [m]
        self.C_P            = self.nabla/(self.C_M*self.L*self.B*self.T_M)  # prismatic coefficient
        self.C_B            = self.nabla/(self.L*self.B*self.T_M)
   