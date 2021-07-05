BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "tblMember" (
	"MemberId"	CHAR(6),
	"FirstName"	VARCHAR(30),
	"LastName"	VARCHAR(30),
	"Phone"	VARCHAR(15),
	PRIMARY KEY("MemberId")
);
CREATE TABLE IF NOT EXISTS "tblActivity" (
	"ActivityCode"	CHAR(6),
	"Description"	VARCHAR(100),
	"Fee"	DECIMAL(13, 2),
	PRIMARY KEY("ActivityCode")
);
CREATE TABLE IF NOT EXISTS "tblAssessor" (
	"AssessorId"	INT,
	"FirstName"	VARCHAR(30),
	"LastName"	VARCHAR(30),
	"EMail"	VARCHAR(30),
	PRIMARY KEY("AssessorId")
);
CREATE TABLE IF NOT EXISTS "tblCertificate" (
	"MemberId"	CHAR(6),
	"ActivityCode"	CHAR(6),
	"DateAssessed"	DATE,
	"AssessorId"	INT,
	PRIMARY KEY("MemberId","ActivityCode"),
	FOREIGN KEY("ActivityCode") REFERENCES "tblActivity"("ActivityCode"),
	FOREIGN KEY("AssessorId") REFERENCES "tblAssessor"("AssessorId"),
	FOREIGN KEY("MemberId") REFERENCES "tblMember"("MemberId")
);
INSERT INTO "tblMember" ("MemberId","FirstName","LastName","Phone") VALUES ('012010','Emily','Marr','01433 181743');
INSERT INTO "tblMember" ("MemberId","FirstName","LastName","Phone") VALUES ('131092','Joe','Donald','01433 910007');
INSERT INTO "tblMember" ("MemberId","FirstName","LastName","Phone") VALUES ('132099','Abdel','Patel','01433 897267');
INSERT INTO "tblMember" ("MemberId","FirstName","LastName","Phone") VALUES ('145543','Precious','Jones','01433 982816');
INSERT INTO "tblMember" ("MemberId","FirstName","LastName","Phone") VALUES ('148765','Jack','Marr','01433 181743');
INSERT INTO "tblMember" ("MemberId","FirstName","LastName","Phone") VALUES ('177455','Ewan','Wilson','01403 234977');
INSERT INTO "tblMember" ("MemberId","FirstName","LastName","Phone") VALUES ('177580','Viran','Ahmed','09828 162534');
INSERT INTO "tblActivity" ("ActivityCode","Description","Fee") VALUES ('DG0011','Digital Citizen',0);
INSERT INTO "tblActivity" ("ActivityCode","Description","Fee") VALUES ('CR0001','Book Binding',0);
INSERT INTO "tblActivity" ("ActivityCode","Description","Fee") VALUES ('DG3002','Digital Photography',20);
INSERT INTO "tblActivity" ("ActivityCode","Description","Fee") VALUES ('SO0112','Public Speaking',0);
INSERT INTO "tblActivity" ("ActivityCode","Description","Fee") VALUES ('SO0201','Animal Welfare',0);
INSERT INTO "tblActivity" ("ActivityCode","Description","Fee") VALUES ('SP8701','Kayaking',30);
INSERT INTO "tblActivity" ("ActivityCode","Description","Fee") VALUES ('CR0020','Puppet Making',7.5);
INSERT INTO "tblActivity" ("ActivityCode","Description","Fee") VALUES ('CR0014','Vegetarian Cookery',7.5);
INSERT INTO "tblAssessor" ("AssessorId","FirstName","LastName","EMail") VALUES (1,'Sue','James','sue.james@me.co.uk');
INSERT INTO "tblAssessor" ("AssessorId","FirstName","LastName","EMail") VALUES (2,'Greta','Geuze','g.geuze@hotmail.com');
INSERT INTO "tblAssessor" ("AssessorId","FirstName","LastName","EMail") VALUES (3,'Mohammed','Franks','m.franks@hotmail.com');
INSERT INTO "tblAssessor" ("AssessorId","FirstName","LastName","EMail") VALUES (4,'Jay','Linton','Jay12@gmail.com');
INSERT INTO "tblAssessor" ("AssessorId","FirstName","LastName","EMail") VALUES (5,'James','Sue','sue.james@me.co.uk');
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('145543','DG0011','21/02/2019',1);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('012010','DG0011','21/02/2019',1);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('132099','DG3002','01/03/2019',2);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('131092','CR0001','15/04/2019',3);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('132099','CR0001','15/04/2019',3);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('012010','CR0001','15/04/2019',3);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('132099','SO0112','02/06/2019',4);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('145543','SO0112','02/06/2019',4);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('148765','SP8701','11/06/2019',2);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('145543','SP8701','01/07/2019',2);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('148765','SO0201','15/08/2019',1);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('132099','SO0201','11/09/2019',1);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('148765','CR0020','12/10/2019',4);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('177455','CR0001','15/12/2019',5);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('177580','CR0001','15/12/2019',5);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('177455','CR0014','24/01/2020',4);
INSERT INTO "tblCertificate" ("MemberId","ActivityCode","DateAssessed","AssessorId") VALUES ('177580','CR0014','24/01/2020',4);
COMMIT;
