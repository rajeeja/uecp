## This python script is created by the RGG AssyGen program in MeshKit ##
# Here the RGG AssyGen program creates the assembly geometry and mesh
#
reset
import cubit
def name_faces(name, body):
    vector_locs = cubit.get_bounding_box("volume", body.id())
    topno = vector_locs[7] - 1e-2
    botno = vector_locs[6] + 1e-2
    cubit.cmd('group "g1" equals surf in vol {0} '.format(body.id()))
    cubit.cmd('group "g2" equals surf  in g1 with z_coord  < {0} and z_coord > {1}'.format(topno,botno))
    cubit.cmd('group  "g3" subtract g2 from g1')
    cubit.cmd('group "gtop" equals surf in g3 with z_coord > {0}'.format(topno) )
    cubit.cmd('group "gbot" equals surf in g3 with z_coord < {0}'.format(botno) )
    g2id = cubit.get_id_from_name("g2")
    ssurfs = cubit.get_group_surfaces(g2id)
    side_surfs = len(ssurfs)
    for i in range(0,side_surfs):
      sname = name + "_side" + str(i+1)
      cubit.cmd('surf {0} name "{1}"'.format( ssurfs[i] , sname )  )
    top_surf = name + "_top"
    bot_surf = name + "_bot"
    cubit.cmd('surf in gtop name "{0}"'.format(top_surf) )
    cubit.cmd('surf in gbot name "{0}"'.format(bot_surf) )
    cubit.cmd('delete group g1 g2 g3 gtop gbot')



def section_assm(cDir, dOffset, szReverse):
    vol = cubit.get_entities("volume")
    for i in range(len(vol)):
      vl = cubit.get_bounding_box("volume", vol[i])
      xmin = vl[0]
      xmax = vl[1]
      ymin = vl[3]
      ymax = vl[4]
      print xmin, xmax, ymin, ymax
      if(xmin > dOffset and cDir == "x" and szReverse == "reverse"):
        cubit.cmd('delete vol {0}'.format(vol[i]) )
        continue
      if(ymin > dOffset and cDir == "y" and szReverse == "reverse"):
        cubit.cmd('delete vol {0}'.format(vol[i]) )
        continue
      if(xmax < dOffset and cDir == "x" and szReverse == ""):
        cubit.cmd('delete vol {0}'.format(vol[i]) )
        continue
      if(ymax < dOffset and cDir == "y" and szReverse == ""):
        cubit.cmd('delete vol {0}'.format(vol[i]) )
        continue
      else:
        if (ymax > dOffset and cDir == "y" and ymin < dOffset):
          cubit.cmd('section vol {0} with yplane offset {1} {2}'.format(vol[i], dOffset, szReverse))
        if (xmax > dOffset and cDir == "x" and xmin < dOffset):
          cubit.cmd('section vol {0} with xplane offset {1} {2}'.format(vol[i], dOffset, szReverse))


cubit.cmd('reset')
assms = range(1)
cp_inpins  = []

cells = []
cyls = []
cp_in = []
sub1 = [] 
sub2 = []
cell = cubit.brick( 1.25984, 1.25984, 205.232)
vector = [0, -0, 102.616]
cubit.move( cell, vector)
cells.append(cell)
lid = cells[0].id()
cubit.set_entity_name("body", lid, "coolant" )
name_faces("coolant", cell) 
#
#
cyl = cubit.cylinder(205.232, 0.61214, 0.61214, 0.61214)
cyls.append(cyl)
vector = [0, 0, 102.616]
cubit.move(cyl, vector)
#
#
cyl = cubit.cylinder(205.232, 0.619, 0.619,0.619)
cyls.append(cyl)
vector = [0, 0, 102.616]
cubit.move(cyl, vector)
sub1[:] = []
sub2[:] = []
tmp_vol = cubit.copy_body(cyls[1])
sub1.append(cells[0])
sub2.append(tmp_vol)
sub1[:] = []
sub2[:] = []
cells[0] = tmp_new 
cell = tmp_new
cp_in.append(tmp_new[0])
tmpvol1 = cyls[0]
cp_in.append(tmp_vol1)
lid = tmp_vol1.id()
cubit.set_entity_name("body", lid, "coolant" )
name_faces("coolant", tmp_vol1) 
tmp_vol = cubit.copy_body(cyls[0])
sub1.append(cyls[1])
sub2.append(tmp_vol)
tmp_new = cubit.subtract(sub2, sub1)
sub1[:] = []
sub2[:] = []
cp_in.append(tmp_new[0])
lid = tmp_new[0].id()
cubit.set_entity_name("body", lid, "coolant_blmat1" )
name_faces("coolant_blmat1", tmp_new1) 
cyls[1] = tmp_new
cp_inpins.append([])
cp_inpins[0].append(cp_in[0])
cp_inpins[0].append(cp_in[1])
cp_inpins[0].append(cp_in[2])
cp_in[:] =[]
cells = []
sub1 = [] 
sub2 = []
cell = cubit.brick( 1.25984, 1.25984, 205.232)
vector = [1.25984, -1.25984, 102.616]
cubit.move( cell, vector)
cells.append(cell)
lid = cells[0].id()
cubit.set_entity_name("body", lid, "coolant" )
name_faces("coolant", cell) 
#
#
cyl = cubit.cylinder(205.232, 0.61214, 0.61214, 0.61214)
cyls.append(cyl)
vector = [1.25984, -1.25984, 102.616]
cubit.move(cyl, vector)
#
#
cyl = cubit.cylinder(205.232, 0.619, 0.619, 0.619)
cyls.append(cyl)
vector = [1.25984, -1.25984, 102.616]
cubit.move(cyl, vector)
sub1[:] = []
sub2[:] = []
tmp_vol = cubit.copy_body(cyls[1])
sub1.append(cells[0])
sub2.append(tmp_vol)
sub1[:] = []
sub2[:] = []
cells[n-1] = tmp_new 
cell = tmp_new
cp_in.append(tmp_new[0])
tmpvol1 = cyls[0]
cp_in.append(tmp_vol1)
lid = tmp_vol1.id()
cubit.set_entity_name("body", lid, "coolant" )
name_faces("coolant", tmp_vol1) 
tmp_vol = cubit.copy_body(cyls[0])
sub1.append(cyls[1])
sub2.append(tmp_vol)
tmp_new = cubit.subtract(sub2, sub1)
sub1[:] = []
sub2[:] = []
cp_in.append(tmp_new[0])
lid = tmp_new[0].id()
cubit.set_entity_name("body", lid, "coolant_blmat1" )
name_faces("coolant_blmat1", tmp_new1) 
cyls[1] = tmp_new
cp_inpins.append([])
cp_inpins[0].append(cp_in[0])
cp_inpins[0].append(cp_in[1])
cp_inpins[0].append(cp_in[2])
cp_in[:] =[]
assm = cubit.brick( 2.52, 2.52, 205.232)
vector = [0.62992, -0.62992, 102.616]
cubit.move(assm, vector)
assms.insert(0, assm)
sub1 = []
sub2=[]
lid = assms[0].id()
cubit.set_entity_name("body", lid, "coolant" )
name_faces("coolant", assms[0])
cubit.cmd('group "g1" equals curve in vol {0} '.format(assms[0].id()))
cubit.cmd('group "g2" equals curve with z_max<> z_min in g1')
cubit.cmd('group  "g3" subtract g2 from g1')
tmp_g3id = cubit.get_id_from_name("g3")
gs_curves = cubit.get_group_curves(tmp_g3id)
side_curves = len(gs_curves)
for i in range(0,side_curves):
  sname = "side_edge" + str(i+1)
  cubit.cmd('curve {0} name "{1}"'.format( gs_curves[i] , sname )  )

pin_copy=[]

sub1=[]
sub2=[]

tmp_vol = cubit.copy_body(cp_inpins[0][0])
pin_copy.append(tmp_vol)

sub2.append(cp_inpins[0][0])
tmp_vol = cubit.copy_body(cp_inpins[0][1])
pin_copy.append(tmp_vol)

sub2.append(cp_inpins[0][1])
tmp_vol = cubit.copy_body(cp_inpins[0][2])
pin_copy.append(tmp_vol)

sub2.append(cp_inpins[0][2])
tmp_vol = cubit.copy_body(cp_inpins[0][3])
pin_copy.append(tmp_vol)

sub2.append(cp_inpins[0][3])
tmp_vol = cubit.copy_body(cp_inpins[0][4])
pin_copy.append(tmp_vol)

sub2.append(cp_inpins[0][4])
tmp_vol = cubit.copy_body(cp_inpins[0][5])
pin_copy.append(tmp_vol)

sub2.append(cp_inpins[0][5])
tmp_vol = assms[1]

sub1.append(assms[0])
tmp_new1 = cubit.subtract(sub2, sub1)
tmp_vol = tmp_new1
vol = cubit.get_entities("volume")
vl = cubit.get_total_bounding_box("volume", vol)
zcenter = 0.0
xcenter = (vl[0]+vl[1])/2.0
ycenter = (vl[3]+vl[4])/2.0
cubit.cmd('move vol all x {0} y {1} z {2}'.format(-xcenter, -ycenter, -zcenter) )
cubit.cmd('export acis "q.sat" over')
