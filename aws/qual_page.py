import boto3
import xml.etree.ElementTree as ET


questions_xml = """
<?xml version="1.0" encoding="utf-8"?>
<QuestionForm xmlns:tns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2017-11-06/QuestionForm.xsd">
  <Overview>
      <Title>Ideology and the Domestic American Economy</Title>
      <Text>Please read the following directions: We are annotating the dimensions of ideology around the topic of the domestic American economy.  
      We will follow the examples in the pre-qualification page; please note that these examples are reproduced below this text for your ease of reference.  
      Start by reading the text below and ask yourself which ideological dimension of the domestic American economy are covered by this text.  
      If you cannot easily situate the dimensions revert back to the examples below.  
      Annotate as many dimensions as possible for each text.  
      If no dimensions apply, for example if the text is about wars or a state budget, then skip the task because it is not about the domestic American economy. Single word answers can be tricky to annotate.  
      When they  are broad, like for example, “economy”  they  are meaningless because we are not sure what the author is conveying with this broad term. 
      Hence, the task should be skipped. However, some single word answers, like for example, “the deficit”, are more meaningful because the text can be understood as the author is against an increase in deficit/budget deficit.  
      In this case, the text should be annotated.
      </Text>
  </Overview>
  <Question>
      <QuestionIdentifier>question1</QuestionIdentifier>
      <IsRequired>true</IsRequired>
      <QuestionContent>
          <Text>Have you read and understood the directions for this task?</Text>
      </QuestionContent>
      <AnswerSpecification>
        <SelectionAnswer>
          <StyleSuggestion>radiobutton</StyleSuggestion>
            <Selections>
              <Selection>
                <SelectionIdentifier>1</SelectionIdentifier>
                <Text>Yes</Text>
              </Selection>
              <Selection>
                <SelectionIdentifier>2</SelectionIdentifier>
                <Text>No</Text>
              </Selection>
            </Selections>
        </SelectionAnswer>
    </AnswerSpecification>
  </Question>
</QuestionForm>"""


answer_xml = """
<?xml version="1.0" encoding="utf-8"?>
<AnswerKey xmlns:tns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/AnswerKey.xsd">
<Question>
        <QuestionIdentifier>question1</QuestionIdentifier>
        <AnswerOption>
            <SelectionIdentifier>1</SelectionIdentifier>
            <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
            <SelectionIdentifier>2</SelectionIdentifier>
            <AnswerScore>0</AnswerScore>
        </AnswerOption>
    </Question>
    <QualificationValueMapping>
        <PercentageMapping>
            <MaximumSummedScore>1</MaximumSummedScore>
        </PercentageMapping>
    </QualificationValueMapping>
</AnswerKey>
"""

#question_file = open('questions.xml', 'r').read()
#xml = question_file.format
#
questions = ET.parse('questions.xml')
q_root = questions.getroot()
question_form = ET.tostring(q_root, encoding='unicode')

answers = ET.parse('answers.xml')
a_root = answers.getroot()
answer_form = ET.tostring(a_root, encoding='unicode')

region_name = 'us-east-1'
aws_access_key_id = 'AKIAVGWXFZ3AB7C4D2VU'
aws_secret_access_key = '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'

endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

# Uncomment this line to use in production
# endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'

client = boto3.client(
    'mturk',
    endpoint_url=endpoint_url,
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

new_qual = client.create_qualification_type(
    Name="Qualification 1",
    Description="Understanding directions",
    QualificationTypeStatus='Active',
    Test=questions_xml, AnswerKey=answer_xml,
    TestDurationInSeconds=600

)

print(type(new_qual))
