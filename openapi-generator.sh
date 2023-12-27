#!/usr/bin/env bash

# Load env variables (in the .env file)
#set -o allexport
#source .env
#set +o allexport

#DEFAULT VALUES
PACKAGE_NAME="usemotion_api_client"
PACKAGE_URL="https://github.com/gitchrisqueen/usemotion-api-client"
PACKAGE_VERSION="1.0.0"
PROJECT_NAME="usemotion_api_client"
ISO_DATE_FORMAT="%Y-%m-%d"
ISO_DATETIME_FORMAT="%Y-%m-%dT%H:%M:%S%z"
USEONEOFDISCRIMINATORLOOKUP="true"
GIT_USER="gitchrisqueen"
GIT_REPO="usemotion-api-client"
CONFIG_OPTIONS="appName=Motion REST API Client,infoName=Christopher Queen,infoEmail=christopher.queen@gmail.com,dateFormat=$ISO_DATE_FORMAT,datetimeFormat=$ISO_DATETIME_FORMAT,packageName=$PACKAGE_NAME,packageUrl=$PACKAGE_URL,packageVersion=$PACKAGE_VERSION,projectName=$PROJECT_NAME,useOneOfDiscriminatorLookup=$USEONEOFDISCRIMINATORLOOKUP"
RELEASE_NOTE="OpenAPI client code auto-generated for version $PACKAGE_VERSION"

pydantic_version="2"
INPUT_FILE="https://stoplight.io/api/v1/projects/motion/motion-rest-api/nodes/swagger.json"
CURRENT_PATH=$(pwd)
generator="python" # Use python | python-pydantic-v1

export PYTHON_POST_PROCESS_FILE="$(which yapf) -i"

read -r -e -p "Which Pydantic version? [$pydantic_version]: " input
pydantic_version=${input:-$pydantic_version}

if [ "$pydantic_version" = "1" ]; then
    generator="python-pydantic-v1"

fi

echo "Using Pydantic version: $pydantic_version | Generator: $generator"

git_tag="p${pydantic_version}_$PACKAGE_VERSION"

# Create pydantic v version of code
echo "Generating v$PACKAGE_VERSION pydantic v$pydantic_version code"
openapi-generator generate --git-host github.com --git-repo-id $GIT_REPO --git-user-id $GIT_USER --enable-post-process-file \
 -g $generator -i $INPUT_FILE -o ./ --additional-properties="$CONFIG_OPTIONS"

exit 1

# Tag and Push
(
echo "Git creating tag $git_tag" && \
git tag "$git_tag" && \
echo "Git pushing tag $git_tag" && \
git push origin "$git_tag"
)
