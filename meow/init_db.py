# Bone-Meat ratio data source: https://www.hannahra.com/2021/02/my-raw-meaty-bone-percentage-spreadsheet.html

import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="meowculator",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'],
    port=6969
)

# Open a cursor to perform db ops
cur = conn.cursor()

# Create table 'chicken'
cur.execute('DROP TABLE IF EXISTS chicken;')
cur.execute('CREATE TABLE chicken (type varchar(20) NOT NULL,'
                                    'meat integer NOT NULL,'
                                    'bone integer NOT NULL,'
                                    'offal integer NOT NULL);'
            )


# Insert chicken data
cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('back',
             '56',
             '44',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('whole-processed',
             '68',
             '32',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('breast',
             '80',
             '20',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('foot',
             '40',
             '60',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('head',
             '25',
             '75',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('leg',
             '73',
             '27',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('leg_quarter',
             '70',
             '30',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('neck_w_skin',
             '64',
             '36',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('neck_wo_skin',
             '25',
             '75',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('ribcage(frames)',
             '20',
             '80',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('thigh',
             '79',
             '21',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('wing',
             '54',
             '46',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('cornish_hen(whole)',
             '61',
             '39',
             '0')
            )

cur.execute('INSERT INTO chicken (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('quinea_hen',
             '83',
             '17',
             '0')
            )

##########################################################################

# Create table 'duck'
cur.execute('DROP TABLE IF EXISTS duck;')
cur.execute('CREATE TABLE duck (type varchar(20) NOT NULL,'
            'meat integer NOT NULL,'
            'bone integer NOT NULL,'
            'offal integer NOT NULL);'
            )

# Insert duck data
cur.execute('INSERT INTO duck (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('whole-processed',
             '72',
             '28',
             '0')
            )

cur.execute('INSERT INTO duck (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('wild_duck',
             '62',
             '38',
             '0')
            )

cur.execute('INSERT INTO duck (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('breast(bone-in)',
             '85',
             '15',
             '0')
            )

cur.execute('INSERT INTO duck (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('foot',
             '40',
             '60',
             '0')
            )

cur.execute('INSERT INTO duck (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('frame',
             '20',
             '80',
             '0')
            )

cur.execute('INSERT INTO duck (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('head',
             '25',
             '75',
             '0')
            )

cur.execute('INSERT INTO duck (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('leg',
             '66',
             '34',
             '0')
            )

cur.execute('INSERT INTO duck (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('neck',
             '50',
             '50',
             '0')
            )

cur.execute('INSERT INTO duck (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('wing',
             '61',
             '39',
             '0')
            )

##########################################################################

# Create table 'lamb'
cur.execute('DROP TABLE IF EXISTS lamb;')
cur.execute('CREATE TABLE lamb (type varchar(20) NOT NULL,'
            'meat integer NOT NULL,'
            'bone integer NOT NULL,'
            'offal integer NOT NULL);'
            )

# Insert lamb data
cur.execute('INSERT INTO lamb (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('chop',
             '85',
             '15',
             '0')
            )

cur.execute('INSERT INTO lamb (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('neck',
             '68',
             '32',
             '0')
            )

cur.execute('INSERT INTO lamb (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('ribs',
             '73',
             '27',
             '0')
            )

##########################################################################

# Create table 'pork'
cur.execute('DROP TABLE IF EXISTS pork;')
cur.execute('CREATE TABLE pork (type varchar(20) NOT NULL,'
            'meat integer NOT NULL,'
            'bone integer NOT NULL,'
            'offal integer NOT NULL);'
            )

# Insert pork data
cur.execute('INSERT INTO pork (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('feet',
             '70',
             '30',
             '0')
            )

cur.execute('INSERT INTO pork (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('neck',
             '50',
             '50',
             '0')
            )

cur.execute('INSERT INTO pork (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('ribs',
             '70',
             '30',
             '0')
            )

cur.execute('INSERT INTO pork (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('tail',
             '70',
             '30',
             '0')
            )

##########################################################################

# Create table 'rabbit'
cur.execute('DROP TABLE IF EXISTS rabbit;')
cur.execute('CREATE TABLE rabbit (type varchar(20) NOT NULL,'
            'meat integer NOT NULL,'
            'bone integer NOT NULL,'
            'offal integer NOT NULL);'
            )

# Insert rabbit data
cur.execute('INSERT INTO rabbit (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('whole-prey',
             '90',
             '10',
             '0')
            )

cur.execute('INSERT INTO rabbit (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('whole-processed',
             '72',
             '28',
             '0')
            )

cur.execute('INSERT INTO rabbit (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('back',
             '85',
             '15',
             '0')
            )

cur.execute('INSERT INTO rabbit (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('front_leg',
             '85',
             '15',
             '0')
            )

cur.execute('INSERT INTO rabbit (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('front_quarter',
             '77',
             '23',
             '0')
            )

cur.execute('INSERT INTO rabbit (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('head',
             '25',
             '75',
             '0')
            )

cur.execute('INSERT INTO rabbit (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('hind_leg',
             '86',
             '14',
             '0')
            )

cur.execute('INSERT INTO rabbit (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('hind_quarter',
             '83',
             '17',
             '0')
            )

##########################################################################

# Create table 'turkey'
cur.execute('DROP TABLE IF EXISTS turkey;')
cur.execute('CREATE TABLE turkey (type varchar(20) NOT NULL,'
            'meat integer NOT NULL,'
            'bone integer NOT NULL,'
            'offal integer NOT NULL);'
            )

# Insert turkey data
cur.execute('INSERT INTO turkey (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('whole-processed',
             '79',
             '21',
             '0')
            )

cur.execute('INSERT INTO turkey (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('back',
             '50',
             '50',
             '0')
            )

cur.execute('INSERT INTO turkey (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('breast',
             '90',
             '10',
             '0')
            )

cur.execute('INSERT INTO turkey (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('foot',
             '40',
             '60',
             '0')
            )

cur.execute('INSERT INTO turkey (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('head',
             '25',
             '75',
             '0')
            )

cur.execute('INSERT INTO turkey (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('leg',
             '62',
             '38',
             '0')
            )

cur.execute('INSERT INTO turkey (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('neck',
             '58',
             '42',
             '0')
            )

cur.execute('INSERT INTO turkey (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('tail',
             '90',
             '10',
             '0')
            )

cur.execute('INSERT INTO turkey (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('thigh',
             '80',
             '20',
             '0')
            )

cur.execute('INSERT INTO turkey (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('wing',
             '67',
             '33',
             '0')
            )

##########################################################################

# Create table 'others'
cur.execute('DROP TABLE IF EXISTS others;')
cur.execute('CREATE TABLE others (type varchar(20) NOT NULL,'
            'meat integer NOT NULL,'
            'bone integer NOT NULL,'
            'offal integer NOT NULL);'
            )

# Insert others data
cur.execute('INSERT INTO others (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('dove(whole)',
             '77',
             '23',
             '0')
            )

cur.execute('INSERT INTO others (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('goose(whole)',
             '81',
             '19',
             '0')
            )

cur.execute('INSERT INTO others (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('pheasant(whole)',
             '86',
             '14',
             '0')
            )

cur.execute('INSERT INTO others (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('quail(whole)',
             '90',
             '10',
             '0')
            )

cur.execute('INSERT INTO others (type, meat, bone, offal)'
            'VALUES (%s, %s, %s, %s)',
            ('squab(pigeon)',
             '77',
             '23',
             '0')
            )

##########################################################################

conn.commit()

cur.close()
conn.close()