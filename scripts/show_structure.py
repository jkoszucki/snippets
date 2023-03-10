from pathlib import Path

# temperate phages
# names = ['1007_NOWAYS.7746_PROTEIN_51','1008_AMALTHEA.4455_PROTEIN_80','1019_DISTILL.5026_PROTEIN_69','1021_OTTO.9884_PROTEIN_53','1052_MINERS.8805_PROTEIN_34','1053_SUBBORNED.8408_PROTEIN_60','1056_SPLITS.7742_PROTEIN_53','1090_MALCOLME.1819_PROTEIN_57','1091_PITILESS.2059_PROTEIN_143','1091_PITILESS.2059_PROTEIN_144','1091_PITILESS.2059_PROTEIN_44','1092_BREAKFASTING.1668_PROTEIN_34','1220_GAZITES.0725_PROTEIN_55','1221_THWARTING.7905_PROTEIN_33','1230_PATRONS.9860_PROTEIN_50',\
# '1230_PATRONS.9860_PROTEIN_58','1231_OBTRUDING.4792_PROTEIN_45','1248_GLUM.9648_PROTEIN_57','1271_JOKMEAM.8795_PROTEIN_47','1402_VITALS.4711_PROTEIN_57','1406_DISSOLUTION.1441_PROTEIN_54','1438_DISSOLUTION.9161_PROTEIN_62','1489_BOWER.5541_PROTEIN_45','1489_BOWER.5541_PROTEIN_48','1489_BOWER.5541_PROTEIN_53','1491_ABSINTHE.6518_PROTEIN_65','1507_TRENCHER.0700_PROTEIN_77','1508_FEATURELESS.6449_PROTEIN_37','1508_FEATURELESS.6449_PROTEIN_38','1537_SABLE.5352_PROTEIN_57',\
# '1538_BESTIR.0110_PROTEIN_54','1606_PRACTICE.4544_PROTEIN_69','1606_PRACTICE.4544_PROTEIN_70','1609_DISENGAGEMENT.9480_PROTEIN_69','1611_OVERGROWTH.4977_PROTEIN_38','1630_MOCKERS.2666_PROTEIN_70','1631_INCENSE.0313_PROTEIN_43','1631_INCENSE.0313_PROTEIN_52','1663_MUTENESS.7285_PROTEIN_69','1664_LULLED.1879_PROTEIN_74','1666_AGREEABLE.0191_PROTEIN_44','1668_MILCHE.4528_PROTEIN_49','1668_MILCHE.4528_PROTEIN_52','1715_SHAVED.3653_PROTEIN_54','1715_SHAVED.3653_PROTEIN_57',\
# '1718_KNOCKED.0774_PROTEIN_36','1723_CAMPHORATED.7654_PROTEIN_62','1724_LECHERIE.7652_PROTEIN_71','1815_SHASTA.3560_PROTEIN_56','1819_UNINTENTIONALLY.9452_PROTEIN_50','1819_UNINTENTIONALLY.9452_PROTEIN_53','1820_DISCONTENTS.4844_PROTEIN_42','1820_DISCONTENTS.4844_PROTEIN_44','1823_CONCEPTION.9006_PROTEIN_43','1825_UNCOMELY.7576_PROTEIN_52','1849_SUBSCRIBED.8635_PROTEIN_60','1863_REPAIR.8842_PROTEIN_75','1920_AGREE.6447_PROTEIN_60','1920_AGREE.6447_PROTEIN_71','1920_AGREE.6447_PROTEIN_74',\
# '1923_NEERELY.5665_PROTEIN_54','1930_CLOTTING.7012_PROTEIN_74','1944_SPROUT.8074_PROTEIN_75','245_SIGNIFICANCY.7679_PROTEIN_48','246_RAGGES.6132_PROTEIN_71','248_TIGERISH.0661_PROTEIN_38','248_TIGERISH.0661_PROTEIN_43','24_DEVISING.7682_PROTEIN_54','277_ORATOR.0792_PROTEIN_47','278_WHIRRING.9798_PROTEIN_42','278_WHIRRING.9798_PROTEIN_59','279_SHUHAMITES.8277_PROTEIN_60','316_MINIONS.8624_PROTEIN_59','316_MINIONS.8624_PROTEIN_60','320_WEYWARD.4366_PROTEIN_65','321_MEHUNIMS.0091_PROTEIN_71',\
# '321_MEHUNIMS.0091_PROTEIN_74','347_TRANSFORMED.9797_PROTEIN_74','348_IDLING.0379_PROTEIN_88','348_IDLING.0379_PROTEIN_89','409_INCOMPUTABLE.6909_PROTEIN_39','409_INCOMPUTABLE.6909_PROTEIN_46','434_ORBICULAR.5374_PROTEIN_33','435_CONJURING.3146_PROTEIN_73','439_ETRE.3862_PROTEIN_41','440_NEWTRALL.1444_PROTEIN_59','440_NEWTRALL.1444_PROTEIN_66','441_LIPPES.4295_PROTEIN_44','453_DELICACY.9048_PROTEIN_72','453_DELICACY.9048_PROTEIN_73','460_ULAI.6658_PROTEIN_66','461_VILLAINS.1277_PROTEIN_36',\
# '535_GIRGASHITES.5161_PROTEIN_1','616_APPII.0193_PROTEIN_34','616_APPII.0193_PROTEIN_42','617_ORNAMENTS.5974_PROTEIN_76','617_ORNAMENTS.5974_PROTEIN_77','651_WARRES.0500_PROTEIN_40','665_UNANNOUNC.7897_PROTEIN_54','666_DERBY.9359_PROTEIN_77','666_DERBY.9359_PROTEIN_78','666_DERBY.9359_PROTEIN_83','688_PEDAHZUR.1773_PROTEIN_17','699_COMMING.5719_PROTEIN_61','706_ABIDAH.9693_PROTEIN_38','735_SOUNDS.1369_PROTEIN_75','736_UNTROUBLED.0807_PROTEIN_54','739_WAFTER.2065_PROTEIN_40',\
# '744_APPALL.9480_PROTEIN_75','793_ICEBERG.6642_PROTEIN_49','794_SEEMED.3753_PROTEIN_54','797_BLOCKHEADS.5729_PROTEIN_77','851_MEMBRANES.5213_PROTEIN_53','851_MEMBRANES.5213_PROTEIN_67','861_TROUBLER.6602_PROTEIN_71','876_MAPPLE.0056_PROTEIN_60','914_ZIPPORAH.7916_PROTEIN_74','914_ZIPPORAH.7916_PROTEIN_77','964_LAGOON.2181_PROTEIN_65','984_GERMAINE.3013_PROTEIN_57']
# structures_dir = '/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/DATABASES/KASPAH/KASPAH_2020-01/3_DEPO_AF2/'

# lytic phages
names = ['PUTATIVE_RBP_LYTIC_10','PUTATIVE_RBP_LYTIC_11','PUTATIVE_RBP_LYTIC_12','PUTATIVE_RBP_LYTIC_13','PUTATIVE_RBP_LYTIC_14','PUTATIVE_RBP_LYTIC_16','PUTATIVE_RBP_LYTIC_17','PUTATIVE_RBP_LYTIC_19','PUTATIVE_RBP_LYTIC_2','PUTATIVE_RBP_LYTIC_22','PUTATIVE_RBP_LYTIC_24','PUTATIVE_RBP_LYTIC_25','PUTATIVE_RBP_LYTIC_26','PUTATIVE_RBP_LYTIC_27','PUTATIVE_RBP_LYTIC_28','PUTATIVE_RBP_LYTIC_29','PUTATIVE_RBP_LYTIC_3','PUTATIVE_RBP_LYTIC_31','PUTATIVE_RBP_LYTIC_32','PUTATIVE_RBP_LYTIC_33', \
         'PUTATIVE_RBP_LYTIC_35','PUTATIVE_RBP_LYTIC_4','PUTATIVE_RBP_LYTIC_43','PUTATIVE_RBP_LYTIC_44','PUTATIVE_RBP_LYTIC_45','PUTATIVE_RBP_LYTIC_46','PUTATIVE_RBP_LYTIC_54','PUTATIVE_RBP_LYTIC_55','PUTATIVE_RBP_LYTIC_56','PUTATIVE_RBP_LYTIC_57','PUTATIVE_RBP_LYTIC_58','PUTATIVE_RBP_LYTIC_59','PUTATIVE_RBP_LYTIC_6','PUTATIVE_RBP_LYTIC_60','PUTATIVE_RBP_LYTIC_61','PUTATIVE_RBP_LYTIC_62','PUTATIVE_RBP_LYTIC_63','PUTATIVE_RBP_LYTIC_64','PUTATIVE_RBP_LYTIC_65','PUTATIVE_RBP_LYTIC_66', \
         'PUTATIVE_RBP_LYTIC_67','PUTATIVE_RBP_LYTIC_68','PUTATIVE_RBP_LYTIC_7','PUTATIVE_RBP_LYTIC_71','PUTATIVE_RBP_LYTIC_74','PUTATIVE_RBP_LYTIC_8','PUTATIVE_RBP_LYTIC_9']
structures_dir = '/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/COLLABORATORS/LYTIC_RBP'

# paths & params
i = 46
name = names[i]
file = str(Path(structures_dir, f'{name}.pdb'))

# pymol
print( f'Load structure {name}.pdn (index {i}) ...') # start

print('Hide old structures! ', end='')
cmd.disable()
print('Done!')

print('Load structure! ', end='')
cmd.load(file)
print('Done!')

print('Show structure! ', end='')
cmd.enable(name)
print('Done!')

print('Color by b factor. ', end='')
cmd.spectrum(expression='b')
print('Done!')

print('Reset view. ', end='')
cmd.reset()
print('Done!')

### snippets

# print('Rotate structure!', end='')
# help(cmd.rotate)
# for i in range(3):
#     cmd.rotate(axis='x', angle=30, object=n)
#     sleep(1)
#
# print('Done!')

# print('Hide structure! ', end='')
# cmd.disable(n)
# print('Done!', end='')


# 31, 32, 33, 119 corbohydrate binding
# 61 toxin antitoxin?
